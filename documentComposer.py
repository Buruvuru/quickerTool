from quickerTool import *
import os
#default path for QuickerTools
path="/Users/Zeno Maximus/Documents/quickerTools-projects"

#Upon opening , document composer must create a text file and open it with the system default editor

#Steps :
#1. Check if quickerTool-projects folder exists in documents
isExist=os.path.exists(path)
print(isExist)
#2. If not exist, create quicktools project folder
#3. If exist check the folder contents and display them on screen for user choose one
#4. If user does not want to operate on a recent project , but rather a new project,
# give the user the option to create new project.
#5.Associate new project with a folder, allow the user to name this folder.


#Side Notes

#Make quicktools folder the parent directory
#For every new path , join the new folder to the parent directory