from quickerTool import *
import mmap
currentFile=open("index.txt",'r')
#tagStream is the list in which html is stored after being converted from tagless
#The list will be converted to string and saved as html.

tagStream=[]

#code to write doctype tag
#on the left side of the = is the keyword
webpage="webpage"
with open(r'index.txt','rb',0) as file:
    s=mmap.mmap(file.fileno(),0, access=mmap.ACCESS_READ)
    if s.find(b'webpage')!=-1:
        print('string exists in file')
        repla=doctypeTag()
        tagStream.append(repla)


#code to write title tag
title="title"
for title in currentFile:
    repla=titleTag("We are here")
    tagStream.append(repla)


#below is a function to send tagStream to compiler
#def sendTagStream():
    #sentStream=tagStream
    #return sentStream

#make a string  from tagStream
readyCode=(tagStream)
print(readyCode)




