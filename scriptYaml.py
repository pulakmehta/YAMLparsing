'''
Author: Pulak Mehta
Date: April 18,2021
Version: 1.0

Overview:
This YAML merging function has been broken down into smaller functions and in the logic flow is as follows -
1) __init__ - This defines the path of the leaf YAML file
2) main() - Data first goes to the main() function. If the path is valid, it sends it to the filesToParse()
3) filesToParse - In this function goes recursive calls to prepare a list of YAML files needs to be parsed. It stops when no file name is found parent document
4) mergingFiles - In this function, files are selected one-by-one from child to parent, to be merged. It sends the currently merged file and next file to be merged as inputs to the next function
5) mergeIndividualYamls - This is where the actual merging happens based on the following rules -
5.1) If the existing merged YAML is empty, it returns the other YAML file (may/maynot be empty)
5.1) If both are list, then append
5.2) If currently merged is list, then the other YAML is concatenated
5.3) If existing merged YAML and next YAML file are a key-value pair, if keys are present in both, a recurrsive call is made to the function for further analysis
5.4) If existing merged YAML and next YAML file are a key-value pair, if keys are unique to next YAML, them the child's value is added to parent's value
6) printingFinal - The final step after these calls, is to stdout and return using this function

=> Limitations identified: This code may not work for placeholders in YAML like {{session.state}}

More documentation - https://github.com/pulakmehta/YAMLparsing
'''
import yaml 
import os.path
import sys
from os import path

class MergingScript:
    def __init__(self, yamlPath):
        '''initiates the location of the child (final) YAML'''
        self.pathLocation = yamlPath

    def printingFinal(self, yamlOutput):        
        '''Prints the final merged YAML files''' 
        yaml.dump(yamlOutput,sys.stdout)            # Prints YAML file
        return yamlOutput                           # Returns the YAML file for outside function to process

    def mergeIndividualYamls(self, yaml_1,yaml_2):  
        '''this function merges two yaml file togerther. It mergers YAML_1(merged until now) into YAML_2(latest file)'''
        try:
            if yaml_1==None:
                yaml_1 = yaml_2
                
            elif isinstance(yaml_1, list):          # check if YAML 1 is a list
                if isinstance(yaml_2, list):        # check if YAML 2 is a list
                    yaml_1.extend(yaml_2)           # If both list, then adds the item one-by-ont
                else:
                    yaml_1.append(yaml_2)           # Else, adds elements from YAML 2 as a single item at the end of YAML 1 
            elif isinstance(yaml_1, dict):          # Check if YAML 1 is a dictionary (key-value pair)     
                if isinstance(yaml_2, dict):        # Check if YAML 2 is a dictionary (key-value pair)
                    for key in yaml_2:
                        if key in yaml_1:           # Items present in both YAMLS
                            yaml_1[key] = self.mergeIndividualYamls(yaml_1[key], yaml_2[key])  #Recurrsive call to parse and join
                        else:
                            yaml_1[key] = yaml_2[key] #Child value is copied into the parent value
        except:
            print ("Error 3: Error in merging in ",yaml_2 ,". Please check if it follows YAML format") #Error that there is an issue in merging the files
            raise TypeError
        return yaml_1


    def mergingFiles(self,fileList):
        '''This function loads YAML files one-by-one and joins them starting from the most inner file to the parent file'''
        num = len(fileList)
        i = 0
        temp = 0
        with open(fileList[0]) as file:                             #load the first YAML file
            fromYaml = yaml.load(file, Loader=yaml.FullLoader)
            
        while i < num-1:
            with open(fileList[1]) as file:                         #Loop thru all YAML files to be merged
                toYaml = yaml.load(file, Loader=yaml.FullLoader)    #Load next YAML file
            fromYaml = self.mergeIndividualYamls(fromYaml,toYaml)   #Merging YAML files one-by-one
            i = i+1
        return self.printingFinal(fromYaml)                         #Call printing function to print the final YAML files

    def filesToParse(self):
        '''This function creates a list of YAML files that would have to be merged'''
        try:
            fileList = []                                       
            fileList.append(self.pathLocation)                  

            tempPath = os.path.split(self.pathLocation)                     #Path of the last file split into file name and location
            temp = os.path.join(os.path.split(tempPath[0])[0],tempPath[1])  # Directory location of the last file

            while (path.isfile(temp)==True):
                fileList.append(temp)                                       # Create list of YAML files to be merged
                temp2 = os.path.split(os.path.split(temp)[0])[0]            # Extracting the directory of the parent folder
                temp = os.path.join(temp2[0],tempPath[1])                   # Merging directory of the parent folder and the file name, would be checked in the next loop
            return self.mergingFiles(fileList)
            
        except:
            print ("Error 2: Some files may have error. Please check if they are in YAML format")
            raise TypeError

        return ()

    def main(self):
        try:
            if (path.isfile(self.pathLocation)==True):
                return self.filesToParse()
            
            else:
                print("Error 1: The location of the child YAML file couldn't be found. The user should recheck the directory provided")
                raise TypeError
                return ()

        except TypeError:
            return ()
            
if __name__== "__main__":
    path_file = (r".\TestCase\0\test0.docx")
    MergingScript(path_file).main()
