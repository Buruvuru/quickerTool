from quickerTool import *
import os
#function to set name of the path

#default projects folder
defDir="/qtoprojects"


#function to make default path
def makeDefPath(defpath):
    path = defpath
    os.mkdir(path)

#function to create a folder(excluding default path)
def makeFolder(folderName,defpath):

    path=os.path.join(defpath,folderName)
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
projectsFolder=defDir
doesItExist=verifyPath(projectsFolder)
if doesItExist is True:
    rootdir = projectsFolder
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            print(d)
    #if the projects folder does not exist, below is the function to create one
    else:
        setProjectDir=makeDefPath(defDir)


