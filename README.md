# YAMLparsing
- Overview: This code is used to merge YAML files together based on the following conditions:
  - Int/Float/String of the child overwrites the parent, if common. Else, both get included
  - List of parent and child get appended
  - Dictionary gets merged based on the keys. If common, child overwrites the parent. Else, both get included
  - Everything else gets elimated (like comments)
- Version: 1.0
- Author: Pulak Mehta
- Email: pulak.mehta@nokia.com
- Date: April 19,2021
- Objective: This script can merge children and parent YAML files. More details here - 
- Coding language used: Python 3.9.1
- Operating System: Nokia Win10 PC
- Dependencies: 
  - Please ensure that the PyYAML python library is installed 
- Files included:
  - scriptYaml.py: This file contains the merging program. Users need to call
  - testing.py: Contains the code used to perform the testing
  - Travis.yaml: This file contains the code to test on YAML
  - TestCase: # Contains all the test case
     -  Given: 4 test cases provided in the prompt (int/float/string, lists, nested key-value, sister folder)
     -  Merge: YAML files for testing the deeper testing of the merging functionality
    
  
# Error codes (key error codes in the code and their meaning)
 - Error 1: The location of the child YAML file couldn't be found. The user should recheck the directory provided 
 - Error 2: There was an issue in merging the YAML file. Please check the YAML file format
 - Error 99: Unknown error was encountered. Please email support@support.com with you case for further investigation
