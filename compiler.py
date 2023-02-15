from constants import sendTagStream
#while True:
    #with open("welcome.html",'r+') as f:
        #contents = f.readlines()
        #print(contents)

recievedStream=sendTagStream()
str.join(recievedStream)
