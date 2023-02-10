from quickerTool import *
import os
#function to set name of the path
def makeFolder():
    path=input("To begin, please enter the path to your project folder")
    os.mkdir(path)

#function to verify if path exists
def verifyPath(path):
    isExist=os.path.exists(path)
    return isExist


