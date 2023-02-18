from quickerTool import *
htdoc=["<!-- Write your comments here -->"]
documentName="untitled"
#Function to read file into list
def readFile(fileToRead,oldlist):
    with open(fileToRead) as f:
        lines=f.read().splitlines()
        oldlist.append(lines)
#Function to load progress
def progress(list):
    for line in list:
        print(line)

while True:
    text=input('quickerTool Command > :')
    #print("Next Command. Type commit to effect changes!")
    #TRAVERSING FUNCTIONS
    #1. Function to Check if html head is present

    #compare language constants with entered text.
    if text=="doctype":
        doctype = doctypeTag()
        print(doctype)
        htdoc.append(doctype)
    elif text=="title":
        title = titleTag(input("Title of your page"))
        htdoc.append(title)
    elif text=="htmlopen":
        htmlopen=openingHeadTag()
        htdoc.append(htmlopen)
    elif text=="htmlclose":
        htmlclose=closingHtmlTag()
        htdoc.append(htmlclose)

    elif text=="para":
        para=paraTag(input("Type Paragraph "))
        htdoc.append(para)
    elif text=="docname":
        documentName=input("Enter name of new file")
        f=open("%s.html"%documentName,'wb')

        #Trigger
    elif text=="commit":
        conv=''.join(htdoc)
        f=open("%s.html"%documentName,'a')
        f.writelines(conv)
    #work on existing file
    elif text=="openexisting":
        existingFilename=input("Name of Existing File")
        documentName=existingFilename
        readFile(documentName,htdoc)
        progress(htdoc)
    else:
        print("Unrecognized command")






















