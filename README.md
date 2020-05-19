## NLP_Redaction-of-Text-Files

## Author: Purushotham Vadde

## Packages Required for Project:
- nltk
- glob
- re
- argparse
- pytest

In this project i am taking the text files of different formats such as .txt or .md files as input and redacting the senstive data such as names, gender, and other information so that the senstive data will be redacted. 

The projects have below files: 
## 1.main.py 

The main.py accept the multiple input arguments, the project1.py is imported into main.py file and execute the below functions by function calling through main.py. 
- By using the argparser package we create a object by the name parser and add the input arguments by using the add_argument method
- Below are the input arguments that we are going to add by using the add_argument method.
  1. --input
  2. --names
  3. --gender
  4. --date
  5. --concept
  6. --output
  7. --stats
 - The input arguments are passed as input to the redactor methods by importing the redacor package.
 
 
 ## 2. project1.py
 
 The project file contains the below functions
 
 ### **Reading_input(inputfiles)**
 In this function takes inputfiles as argument the inputfiles contain the files passed through the --input argument from the terminal,     below nested list is the example of input argument  
 
 > [['*.txt'], ['otherfiles\\TEXTFILE2.md']]
 
 After flattening the nested list by using the **glob** package we read the files names which are in the list, we read the data from each file and we append it to the list called file_data.
 
 ### **redact_names(files_data)**
 The redact_names(file_data) method takes the input argument as file_data which is from the Reading_input method, the file_data is a list of size with number of input files, we will iterate through each element[list] in the list and convert the each list into words using **nltk.word_tokenize()** the tokenize words are sent to the **nltk.pos_tag()** which tags the words based on tags and the tag words are passed to the **nltk.ne_chunk** which convert the tagged words into chunk based on label example PERSON ,ORGANIZATION etc
 
 >words = nltk.word_tokenize(temp_file)  \
  tagged = nltk.pos_tag(words)    \
  namedEnt = nltk.ne_chunk(tagged)   \
  chunk.label() == 'PERSON'
  
from the labeled chunks we select the tree with label of PERSON which contain the names.we take the person names into the list and based on the list we replace the names in the text with '\u2588' so that the names will be redacted. after execution of the redacted_names method we will get the list with redacted names.
 
 ### **redact_gender(files_data)**
 
 From the above method we will get the list with redacted names which is passed as input parameter to the redact_gender(files_data) method, in this mehtod we declare the list of genders as below:
 
 >genders = ['husband', 'she','herself','woman','him','men', 'his','women', 'male', 'her', 'hers', 'man', 'he','himself', 'female', 'wife']
 
 we will iterate through each element[list] in the list and each element is list and we convert the each list into words using **nltk.word_tokenize()** and we compare the each tokenize word with genders list if both are equal then we are replacing the tokenize words with the '\u2588' so that the genders will be redacted.
 
  ### **redact_date(files_data)**
 The redacted list from the above method is passed as input to the **redacted_date()** method, in this method we are using the below re expession to redact the dates
 
> temp_dates = re.findall(r"\s\w*\s\d\d,\s\d\d\d\d\s", temp_file)
> temp_dates = re.findall(r"\s\d\d\s\w*\s\d\d\d\d", temp_file)

We will find the dates which matches the above regular expression and redacted with '\u2588'.


### **redact_concept(files_data,concept)**
The Redact_concept method takes the redacted_dates list and a concept word as input parameter, By using the **wordnet.synsets(concept)**
method from nltk we will ge the all synonym words for the concept word and stored in synonyms_list, we will iterate through the each element[list] in the nested list and we convert the each element list into token sentences by using the below method in nltk.

>token_sent = nltk.sent_tokenize(temp_file)

if any sentence in the token_sent has the word in the synonyms_list the sentence will be redacted by using '\u2588'.


### **redacted_stats(redacted_type= 'none', count=0)**

The redacted_stats method takes two input arguments as input in each method the redacted text count is passed to redacted_stats method after the redaction of text is done. 
the redacted_stats method takes the count and the redacted type added to the stats_list.

>temp = "The count of " + redacted_type + " : " + str (count) \
>stats_list.append(temp)
 
### **Update_Output(inputfiles,files_data,outputpath)**

The Update_output method takes the inputfiles,files_data,outputpath 3 arguments as input 

- The inputfiles contain the files list we read the names of each file and update the each file names as below adding the .redacted in the file name
>if '.txt' in  input_files[j] \
input_files[j] = input_files[j].replace(".txt", ".redacted.txt") \
if '.md' in input_files[j] \
input_files[j] = input_files[j].replace(".md", ".redacted.txt") 

- the outputpath arugument has folder name where the output redacted files will be stored the path will accessed by using the os package
and below code is used to open the path and create the readacted text files.
>path1 = (os.getcwd()) \
path2 = (outputpath+'/'+filenames[j]) \
final_file = open(os.path.join(path1,path2), "w" ,encoding="utf-8")

-once the text files are created and opened the files_data contain the list of redacted data, we will iterate through the each element in the list and write the data into redacted text files.
>final_file.write(file_data) \
 final_file.close()


### **Update_Redacted_stats(stats_list=stats_list)**
The Update_Redacted_stats(stats_list=stats_list) method takes the input as the stats_list which contain the data of redacted text count, we are creating the stderr.txt file and writing the stats_list data into the stderr.txt file.
>file.write(stats_list[i]) \
file.close()

## 3.test_redactor.py

The test_redactor.py file contains the unit testcases to test each method is working are not which we designed in the redactor.py file, in this file we written the below testcases to test each method. we import the redactor.py file to test access the functions.

### **test_Reading_input()**
  in this method we test the Reading_input(files) method by passing the test data as files =  **[['*.txt'], ['otherfiles\\TEXTFILE2.md']]** 
  
  we will test the test case by checking the the method is returning the list or not. 
> assert type(redactor.Reading_input(files)) == list

### **test_redact_names()**
In this method we are testing the redact_names method by passing the list as input
>list = (redactor.Reading_input(files)) \
redacted_list = redactor.redact_names(list)

The redacted_list contains the redacted names, the redacted_list is passed to nltk.word_tokenize() so that list is converted into token_words and we check the count of redacted words 

>if '\u2588' in j: \
counter += 1

we test the code by assert that counter >0 if the length of counter>0  then the test case will pass else the test case will fail. 
>assert counter is not None


### **test_redact_gender()**
In this method we are testing the redact_gender method by passing the list as input
>list = (redactor.Reading_input(files)) \
redacted_list = redactor.redact_gender(list)

The redacted_list contains the redacted gender, the redacted_list is passed to nltk.word_tokenize() so that list is converted into token_words and we check the count of redacted words 

>if '\u2588' in j: \
counter += 1

we test the code by assert that counter >0, if the length of counter>0  then the test case will pass else the test case will fail.
>assert counter is not None

### **test_redact_date()**
In this method we are testing the redact_date method by passing the list as input
>list = (redactor.Reading_input(files)) \
redacted_list = redactor.redact_date(list)

The redacted_list contains the redacted date, the redacted_list is passed to nltk.word_tokenize() so that list is converted into token_words and we check the count of redacted words 

>if '\u2588' in j: \
counter += 1

we test the code by assert that counter >0, if the length of counter>0  then the test case will pass else the test case will fail.
>assert counter is not None

### **test_redact_concept()**
In this method we are testing the redact_date method by passing the list and concept word as input
>list = (redactor.Reading_input(files)) \
redacted_list = redactor.redact_concept(list,word)

The redacted_list contains the redacted concept word, the redacted_list is passed to nltk.word_tokenize() so that list is converted into token_words and we check the count of redacted words 

>if '\u2588' in j: \
counter += 1

we test the code by assert that counter >0,if the length of counter>0  then the test case will pass else the test case will fail.
>assert counter is not None

### **test_redacted_stats()**
In this method we test the redacted_stats method by len of ststs_list > 0, then the test case will pass else the test case will fail  
assert stats_list is not None


## 4.Assumptions/Bugs:

- In this project i assumed that the date will be in below format any dates aprt from the below format wont be redacted inthis project.
1.March 26, 1930 \
2.26 March, 1930


## Steps to Run project1

- **Step1** \
clone the project directory using below command 
> git clone https://github.com/PurushothamVadde/NLP_Redaction-of-Text-Files.git

- **Step2** \
Navigate to directory that we cloned from git **NLP_Redaction-of-Text-Files / project1** and run the below command by providing URL

>python main.py --input *.txt --input  otherfiles\TEXTFILE2.md  --names  --gender  --dates  --concept  good  --output  files  --stats

- **Step3** 

From **NLP_Redaction-of-Text-Files** run the below command to test the testcases. 

> pytest -v






