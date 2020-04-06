from project1 import redactor
import nltk

files =  [['*.txt'], ['otherfiles\\TEXTFILE2.md']]


def test_Reading_input():
    files_data = (redactor.Reading_input(files))
    assert type(redactor.Reading_input(files)) == list
    for i in range(len(files_data)):
        temp_file = files_data[i]
        assert (len(temp_file)) > 10
    return 0


def test_redact_names():
    counter = 0
    list = (redactor.Reading_input(files))
    redacted_list = redactor.redact_names(list)
    # print(len(redacted_list))
    for i in range(len(redacted_list)):
        temp_file = redacted_list[i]
        words = nltk.word_tokenize(temp_file)
        for j in words:
            # print (j)
            if '\u2588' in j:
                counter += 1
    assert counter is not None

def test_redact_gender():
    counter =0
    list = (redactor.Reading_input(files))
    redacted_list = redactor.redact_gender(list)
    # print(len(redacted_list))
    for i in range(len(redacted_list)):
        temp_file = redacted_list[i]
        words = nltk.word_tokenize(temp_file)
        for j in words:
            # print (j)
            if '\u2588' in j:
                counter += 1
    assert counter is not None

def test_redact_date():
    counter =0
    list = (redactor.Reading_input(files))
    redacted_list = redactor.redact_date(list)
    # print(len(redacted_list))
    for i in range(len(redacted_list)):
        temp_file = redacted_list[i]
        words = nltk.word_tokenize(temp_file)
        for j in words:
            # print (j)
            if '\u2588' in j:
                counter += 1
    assert counter is not None


def test_redact_concept():
    word ='good'
    counter =0
    list = (redactor.Reading_input(files))
    redacted_list = redactor.redact_concept(list,word)
    print((redacted_list))
    for i in range(len(redacted_list)):
        temp_file = redacted_list[i]
        words = nltk.word_tokenize(temp_file)
        for j in words:
            # print (j)
            if '\u2588' in j:
                counter += 1
    assert counter is not None


def test_redacted_stats():
    a = redactor.Reading_input(files)
    a = redactor.redact_names(a)
    a = redactor.redact_gender(a)
    a= redactor.redact_date(a)
    word = 'good'
    redactor.redact_concept(a,word)
    stats_list =redactor.stats_list
    assert stats_list is not None






