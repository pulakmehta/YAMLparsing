# YAMLparsing
- Overview: This code is used to merges YAML files. It takes the directory of the leaf YAML file and recursively merges with immediate parent based on the following conditions:
  - Int/Float/String of the child superseeds the parent. Else, both get included
  - List of the parent and the child get appended
  - Nested key-value pair gets merged based on the keys. Even here the child superseeds the parent
  - Everything else gets elimated (like comments)
- Version: 1.0
- Author: Pulak Mehta
- Email: pulak.mehta@nokia.com
- Date: April 19,2021
- Objective: This script can merge children and parent YAML files. More details here - 
- Coding language used: Python 3.9.1
- Operating System: Nokia Win10 PC
- Dependencies: 
  - Please ensure that the PyYAML python library is installed. To install you may use "pip install pyyaml" 
- Files included:
  - scriptYaml.py: This file contains the merging program. Users need to call
  - testing.py: Contains the code used to perform the testing
  - Travis.yaml: This file contains the code to test on YAML
  - TestCase:
    - 'Integer' number folders contains the test cases
    - 'Expected' contains the expected output of the test cases
    
  
# Error codes (key error codes in the code and their meaning)
 - Error 1: The location of the child YAML file couldn't be found. The user should recheck the directory provided 
 - Error 2: Some files may have error. Please check if they are in YAML format
 - Error 3: There was an issue in merging the YAML file. Please check the YAML file format
 - Error 99: Unknown error was encountered. Please email support@support.com with you case for further investigation
