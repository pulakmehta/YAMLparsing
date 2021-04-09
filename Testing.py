import yaml # Please ensure you have PyYAML installed. This script has been tested for v5.3.1
import os.path
import sys
from os import path

def printing(yamlFile):
    print("5")
    yaml.dump(yamlFile,sys.stdout)

def merge(a,b):
    try:
        if isinstance(a, list):
            # lists can be only appended
            if isinstance(b, list):
                a.extend(b)
            else:
                a.append(b)
        elif isinstance(a, dict):
            # dicts must be merged
            if isinstance(b, dict):
                for key in b:
                    if key in a:
                        a[key] = merge(a[key], b[key])
                    else:
                        a[key] = b[key]
    except:
        print("Error in merging")
        return()
    return a


def merging(fileList):
    num = len(fileList)
    i = 0
    temp = 0
    with open(fileList[0]) as file:
        fromYaml = yaml.load(file, Loader=yaml.FullLoader)
        
    while i < num-1:
        with open(fileList[1]) as file:
            print("3")
            toYaml = yaml.load(file, Loader=yaml.FullLoader)
        fromYaml = merge(fromYaml,toYaml)
        i = i+1
    print("4")
    printing(fromYaml)

def fileToParse(pathlocation):
    #pathlocation = (r"C:\Users\pumehta\Desktop\Coding challenge\a\Testing.py")
    fileList = []           #Contains list of files that would be parsed
    fileList.append(pathlocation)  #Add the provided file into 

    tempPath = os.path.split(pathlocation) 
    temp = os.path.join(os.path.split(tempPath[0])[0],tempPath[1])

    while (path.isfile(temp)==True):
        fileList.append(temp)
        temp2 = os.path.split(os.path.split(temp)[0])[0]
        temp = os.path.join(temp2[0],tempPath[1])
    print("2")
    merging(fileList)

    

def main():
    #pathLocation = input("Please input the path of the child(and last) YAML file to be merged:")
    pathLocation = (r"C:\Users\pumehta\Desktop\Coding challenge\1.yaml")
    try:
        if (path.isfile(pathLocation)==True):
            print("1")
            fileToParse(pathLocation)
            
        else:
            print("Error 1: The path provided has an error")
            return()

    except:
        print("Error 99: There was an unknown error")
        return()

if __name__== "__main__":
   main()


