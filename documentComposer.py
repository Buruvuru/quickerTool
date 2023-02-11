from quickerTool import *
import os
#function to set name of the path

#default projects folder
def defaultPath():
    defpath="C:/qtoprojects"
    return defpath

#function to make default path
def makeDefPath(defpath):
    path = defpath
    os.mkdir(path)

#function to create a folder(excluding default path)
def makeFolder(folderName):
    path=folderName
    os.mkdir(path)
    return path

#function to verify if path exists(can also be used to verify defpath)
def verifyPath(path):
    isExist=os.path.exists(path)
    return isExist

#function to make a file
def makePageSource(name,defpath,path):
    filename=os.path.join(defpath,path,name)
    f=open(filename,"w")


#PROGRAM ENTRY POINT
projectsFolder=defaultPath()
doesItExist=verifyPath(projectsFolder)
if doesItExist is True:


newPage=makePageSource("indeca")
