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
                
            elif isinstance(yaml_1, list):            # check if YAML 1 is a list
                if isinstance(yaml_2, list):        # check if YAML 2 is a list
                    yaml_1.extend(yaml_2)           # If both list, then adds the item one-by-ont
                else:
                    yaml_1.append(yaml_2)           # Else, adds elements from YAML 2 as a single item at the end of YAML 1 
            elif isinstance(yaml_1, dict):          # Check if YAML 1 is a dictionary (key-value pair)     
                if isinstance(yaml_2, dict):        # Check if YAML 2 1 is a dictionary (key-value pair)
                    for key in yaml_2:
                        if key in yaml_1:           # Items present in both YAMLS
                            yaml_1[key] = self.mergeIndividualYamls(yaml_1[key], yaml_2[key])  #Recurrsive call to parse and join
                        else:
                            yaml_1[key] = yaml_2[key] #Parent value replaced with child value if present
        except:
            print("Error 3: Error in merging in ",yaml_2 ,". Please check if it follows YAML format")  #Error that there is an issue in merging the files
            return()
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
            print("Error 2: Some files may have error. Please check if they are in YAML format")
            return ()

    def main(self):
        try:
            if (path.isfile(self.pathLocation)==True):
                return self.filesToParse()
                
            else:
                print("Error 1: The path of the YAML provided has an error. Please check")
                return()
                
        except:
            print("Error 99: There was an unknown error")
            return()

if __name__== "__main__":
    #os.path.join(dirname,r'TestCase\6\test\test','test6.yaml')
    path2 = (r".\TestCase\6\test\test\test6.YAML")
    x = MergingScript(path2)
    x.main()
