## Text Analytics project 1  "Redaction of Text Files"

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
 
 ## **Reading_input(inputfiles)**
 In this function takes inputfiles as argument the inputfiles contain the files passed through the --input argument from the terminal,     below nested list is the example of input argument  
 
 > [['*.txt'], ['otherfiles\\TEXTFILE2.md']]
 
 After flattening the nested list by using the **glob** package we read the files names which are in the list, we read the data from each file and we append it to the list called file_data.
 
 ## **redact_names(files_data)**
 The redact_names(file_data) method takes the input argument as file_data which is from the Reading_input method, the file_data is a list of size with number of input files, we will iterate through each element[list] in the list and convert the each list into words using **nltk.word_tokenize()** the tokenize words are sent to the **nltk.pos_tag()** which tags the words based on tags and the tag words are passed to the **nltk.ne_chunk** which convert the tagged words into chunk based on label example PERSON ,ORGANIZATION etc. from the labeled chunks we select the chunk with label of PERSON which contain the names.we take the person names into the list and based on the list we replace the names in the text with '\u2588' so that the names will be redacted. after execution of the redacted_names method we will get the list with redacted names.
 
 ## **redact_gender(files_data)**
 
 From the above method we will get the list with redacted names which is passed as input parameter to the redact_gender(files_data) method, in this mehtod we declare the list of genders as below:
 
 >genders = ['husband', 'she','herself','woman','him','men', 'his','women', 'male', 'her', 'hers', 'man', 'he','himself', 'female', 'wife']
 
 we will iterate through each element[list] in the list and each element is list and we convert the each list into words using **nltk.word_tokenize()** and we compare the each tokenize word with genders list if both are equal then we are replacing the tokenize words with the '\u2588' so that the genders will be redacted.
 
  ## **redact_date(files_data)**
 The redacted list from the above method is passed as input to the **redacted_date()** method, in this method we are using the below re expession to redact the dates
 
> temp_dates = re.findall(r"\s\w*\s\d\d,\s\d\d\d\d\s", temp_file)
> temp_dates = re.findall(r"\s\d\d\s\w*\s\d\d\d\d", temp_file)

We will find the dates which matches the above regular expression and redacted with '\u2588'.
 
 
 






