import os
import re
import urllib2
import zipfile

data = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/channel.zip")
text = data.read()
with open("channel.zip", "wb") as zFile:
    zFile.write(text)

zFile = zipfile.ZipFile("channel.zip", "r")
cList = []

def chainFollow(nothingValue):
    index = 0
    print str(index) + ": " + nothingValue
    while 1:
        data = zFile.read(nothingValue + ".txt")
        index = index + 1
        found = re.findall("(Next nothing is )([0-9]+)",data)
        if(len(found) > 0):
            nothingValue = found[0][1]
            print str(index) + ": " + nothingValue
            cList.append(zFile.getinfo(nothingValue + ".txt").comment)
        else:
            print "FINISHED"
            answer = ""
            for item in cList:
                answer += item
            print answer
            break


chainFollow("90052")
os.remove("channel.zip")
