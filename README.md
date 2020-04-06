## Text Analytics project 1  "Redaction of Text Files"

## Author: Purushotham Vadde

## Packages Required for Project:
- nltk
- glob
- re
- argparse
- pytest

In this project i am taking the text files of different formats such as .txt or .md files as input and redacting the senstive data such as names, gender, and other information so that the senstive data will be redacted. \

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
 
 






