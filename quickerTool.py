#function to set the Doctype
def doctypeTag():
    tag="<!DOCTYPE html>"
    return tag

#creting title tag
def titleTag(title):
    tag="<title>"+title+"</title>"
    return tag

#opening html tag
def openingHtmlTag():
    tag="<html>"
    return tag

#closing html tag
def closingHtmlTag():
    tag="</html>"
    return tag

#html opening head tag
def openingHeadTag():
    tag="<head>"
    return tag

#html closing head tag
def closingHeadTag():
    tag="</head>"
    return tag

#html opening tag
def openingBodyTag():
    tag="<body>"
    return tag

#html closing body tag
def closingBodyTag():
    tag="</body>"
    return tag

#html attributes ##########################################################3

#a tag with link attribute
def ayTag(link,linkLabel):
    tag="<a href="+link+">"+linkLabel+"</a>"
    return tag

# img tag with src attribute
def imgTag(source,alt):
    tag="<img src="+source+"alt="+alt+">"
    return tag 

# paragraph text
def paraTag(content):
    tag="<p>"+content +"</p>"
    return tag

#br tag
def brTag():
    tag="<br>"
    return tag
#heading tag
def headingTag(number,content):
    tag="<h"+str(number)+">"+content+"</h"+str(number)+">"
    return tag

#more functions to be added

myHeading=headingTag(5,"Welcome")
print(myHeading)

def CreateHtml(title):

    PageName=title
    f=open("%s.html"%PageName,'a')
    return PageName


pagename=titleTag("Welcome Page")

f=open("welcome.html","w")
heading=headingTag(5,"Welcome Home")
f.writelines(heading)

paragraph=paraTag("This is a paragraph created without tags")
f.writelines(paragraph)

image=imgTag("img1.jpg","Nasal Passage")

f.writelines(image)
