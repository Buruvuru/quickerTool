from quickerTool import *
htdoc=["<!-- Write your comments here -->"]
while True:
    text=input('quickerTool Command > :')
    print("Next Command. Type commit to effect changes!")
    #TRAVERSING FUNCTIONS
    #1. Function to Check if html head is present
    def travHead(docObject):
        openTag="<head>"
        closeTag="</head>"
        if openTag not in docObject:
            #need to find the position of the string <!DOCTYPE HTML> and insert head tag just below
            #tonext is the element above the position we want to insert.
            tonext="<!DOCTYPE html>"
            if tonext in docObject:
                pos=tonext.index()
                docObject.insert(openingHeadTag(),pos)
        elif closeTag not in docObject:
            tonext="</title>"
            if tonext in docObject:
                pos=tonext.index()
                docObject.insert(closingBodyTag(),pos)

    #List for generated html

    #Set Language constants

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
    elif text=="commit":
        conv=''.join(htdoc)
        f=open("re.html",'a')
        f.writelines(conv)

#when you resume, try to make each individual function commit on it's own during execution,
#maybe this will enable lines to be written seperately


        print(htdoc)

















