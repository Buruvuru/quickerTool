from quickerTool import *
while True:
    text=input('quickerTool Command > :')
    print(text)

    #Container for generated html
    htdoc=[]
    #Set Language constants

    #compare language constants with entered text.
    if text=="doctype":
        doctype = doctypeTag()
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

print(htdoc)



