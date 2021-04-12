import yaml 
import os.path
import sys
from os import path

class mergingscript:
    def __init__(self, yamlPath):               #define the variable pathlocation of the child (final) file
        self.pathLocation = yamlPath

    def printingFinal(self, yamlOutput):        #print output of the final merged yamls
        yaml.dump(yamlOutput,sys.stdout)
        return yamlOutput

    def mergeIndividualYamls(self, yaml_1,yaml_2):  #merge two files together
        try:
            if isinstance(yaml_1, list):            # check if therei is a list
                if isinstance(yaml_2, list):        # appending if both are a list
                    yaml_1.extend(yaml_2)
                else:
                    yaml_1.append(yaml_2)
            elif isinstance(yaml_1, dict):          
                if isinstance(yaml_2, dict):        # merging of dictionary
                    for key in yaml_2:
                        if key in yaml_1:
                            yaml_1[key] = self.mergeIndividualYamls(yaml_1[key], yaml_2[key])
                        else:
                            yaml_1[key] = yaml_2[key]
        except:
            print("Error2: Error in merging",yaml_1 ,"and", yaml_2)
            return()
        return yaml_1


    def mergingFiles(self,fileList):
        num = len(fileList)
        i = 0
        temp = 0
        with open(fileList[0]) as file:
            fromYaml = yaml.load(file, Loader=yaml.FullLoader)
            
        while i < num-1:
            with open(fileList[1]) as file:
                toYaml = yaml.load(file, Loader=yaml.FullLoader)
            fromYaml = self.mergeIndividualYamls(fromYaml,toYaml)
            i = i+1
        return self.printingFinal(fromYaml)

    def filesToParse(self):
        fileList = []                                       #Contains list of files that would be parsed
        fileList.append(self.pathLocation)                  #Add the provided file into 

        tempPath = os.path.split(self.pathLocation) 
        temp = os.path.join(os.path.split(tempPath[0])[0],tempPath[1])

        while (path.isfile(temp)==True):
            fileList.append(temp)
            temp2 = os.path.split(os.path.split(temp)[0])[0]
            temp = os.path.join(temp2[0],tempPath[1])
        return self.mergingFiles(fileList)

        

    def main(self):
        #pathLocation = input("Please input the path of the child(and last) YAML file to be merged:")
        #pathLocation = ("C:\\Users\\pumehta\\Desktop\\Coding challenge\\1.yaml")
        #try:
        if (path.isfile(self.pathLocation)==True):
            return self.filesToParse()
                
        else:
            print("Error 1: The path provided has an error")
            return()

        #except:
        #   print("Error 99: There was an unknown error")
        #    return()

if __name__== "__main__":
    print("10")
    path2 = (r".\Testcase\1\file\test.yaml")
    x = mergingscript(path2)
    x.main()
