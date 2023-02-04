#function to set the Doctype
def doctypeTag():
    tag="<!DOCTYPE html>"
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



newTag=imgTag("img_girl.jpg" ,"Girl with jacket")
print(newTag)


