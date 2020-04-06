import nltk
import glob
import re
from nltk.corpus import wordnet
import os

stats_list = []

def Reading_input(inputfiles):
    # print(inputfiles)
    files_data = []
    files = nltk.flatten(inputfiles)

    for i in range(len(files)):
        # print(files[i])
        input_files = glob.glob(files[i])
        # print(input_files)
        for j in range(len(input_files)):
            # print(input_files[j])
            data = open(input_files[j]).read()
            # print(data)
            files_data.append(data)
    # print(type(files_data))
    # print(len(files_data))
    return files_data


def redact_names(files_data):
    names_list = []
    NamesRedacted_List = []
    for i in range(len(files_data)):
        temp_file = files_data[i]
        words = nltk.word_tokenize(temp_file)
        tagged = nltk.pos_tag(words)
        # print(tagged)
        namedEnt = nltk.ne_chunk(tagged)
        # namedEnt.draw()
        for chunk in namedEnt:
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    names_list.append(' '.join([c[0] for c in chunk]))
        for names in names_list:
            temp_file = temp_file.replace( names, '\u2588')
        NamesRedacted_List.append(temp_file)
        string = "redacted_names"
        redacted_stats(string,len(names_list))
        names_list.clear()
    # print(NamesRedacted_List)

    return NamesRedacted_List

def redact_gender(files_data):
    gender_list = []
    GenderRedacted_list = []

    genders = ['husband', 'she','herself','woman','him','men', 'his','women',
               'male', 'her', 'hers', 'man', 'he','himself', 'female', 'wife']

    for i in range(len(files_data)):
        temp_file = files_data[i]
        token_words = nltk.word_tokenize(temp_file)
        for words in token_words:
            # print(words)
            for list in genders:
                if words.lower() == list:
                    # print(list)
                    gender_list.append(words)
        for gender in gender_list:
            temp_file = temp_file.replace( " "+gender+" ",  '\u2588')
        GenderRedacted_list.append(temp_file)

        string = "redacted_gender"
        redacted_stats(string, len(gender_list))
        gender_list.clear()
    # print(GenderRedacted_list)

    return GenderRedacted_list

def redact_date(files_data):
    dates_list =[]
    DatesRedacted_list =[]

    for i in range(len(files_data)):
        temp_file = files_data[i]
        temp_dates = re.findall(r"\s\w*\s\d\d,\s\d\d\d\d\s", temp_file)
        dates_list.append(temp_dates)
        temp_dates = re.findall(r"\s\d\d\s\w*\s\d\d\d\d", temp_file)
        dates_list.append(temp_dates)
        for dates in nltk.flatten(dates_list):
                temp_file = temp_file.replace( dates, '\u2588')
        DatesRedacted_list.append(temp_file)

        string = "redacted_dates"
        redacted_stats(string, len(dates_list))
        dates_list.clear()
    # print(DatesRedacted_list)

    return DatesRedacted_list


# concept = "good"
def redact_concept(files_data,concept):
    synonyms_list =[]
    concept_list =[]
    ConceptRedacted_list =[]

    for syn in wordnet.synsets(concept):
        for l in syn.lemmas():
            synonyms_list.append(l.name())
    # print(synonyms_list)

    for i in range(len(files_data)):
        temp_file = files_data[i]
        token_sent = nltk.sent_tokenize(temp_file)
        for sentence in token_sent:
            for synonyms in synonyms_list:
                if synonyms in sentence:
                    concept_list.append(sentence)
        for sentence in concept_list:
            if sentence in temp_file:
                temp_file = temp_file.replace(sentence, '\u2588')
        ConceptRedacted_list.append(temp_file)

        string = "redacted_concept"
        redacted_stats(string, len(concept_list))
        concept_list.clear()
    # print(ConceptRedacted_list)
    # print(stats_list)
    return ConceptRedacted_list


def redacted_stats(redacted_type= 'none', count=0):

    if redacted_type =='redacted_names':
        temp = "The count of " + redacted_type + " : " + str (count)
        stats_list.append(temp)
        # print(stats_list)
    elif redacted_type == 'redacted_dates':
        temp = "The count of " + redacted_type + " : " + str(count)
        stats_list.append(temp)
    elif redacted_type == 'redacted_gender':
        temp = "The count of " + redacted_type + " : " + str(count)
        stats_list.append(temp)
    elif redacted_type == 'redacted_concept':
        temp = "The count of " + redacted_type + " : " + str(count)
        stats_list.append(temp)

    # Update_Redacted_stats(stats_list)
    # print(len(stats_list))
    return stats_list

def Update_Output(inputfiles,files_data,outputpath):
    # print((outputpath))
    filenames =[]
    files = nltk.flatten(inputfiles)
    for i in range(len(files)):
        input_files = glob.glob(files[i])
        # print(input_files)
        for j in range(len(input_files)):
            # print(type(input_files[j]))
            if '.txt' in  input_files[j]:
                input_files[j] = input_files[j].replace(".txt", ".redacted.txt")
            if '.md' in input_files[j]:
                input_files[j] = input_files[j].replace(".md", ".redacted.txt")
            if '\\' in input_files[j]:
                input_files[j]= input_files[j].split("\\")
                input_files[j] = input_files[j][1]
            filenames.append(input_files[j])

    for i in range(len(files_data)):
        for j in range(len(filenames)):
            if i==j:
                file_data =files_data[i]
                # print((file_data))
                # print(outputpath+filenames[j])
                final_file = open(os.getcwd()+ '\\' + outputpath+filenames[j], "w" ,encoding="utf-8")
                final_file.write(file_data)
                final_file.close()
    return len(filenames)


def Update_Redacted_stats(stats_list=stats_list):
    file = open("stderr/stderr.txt", "w")
    for i in range(len(stats_list)):
        file.write(stats_list[i])
        file.write("\n")
    file.close()
    # print(stats_list)
    return stats_list

