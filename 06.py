#!/usr/bin/python3
import os
import re
import urllib.request as urllib
import zipfile

data = urllib.urlopen("http://www.pythonchallenge.com/pc/def/channel.zip")
text = data.read()
with open("channel.zip", "wb") as zFile:
    zFile.write(text)

zFile = zipfile.ZipFile("channel.zip", "r")
cList = []

def chainFollow(nothingValue):
    print("Working...")
    index = 0
    while 1:
        data = zFile.read(nothingValue + ".txt").decode("utf-8")
        index = index + 1
        found = re.findall("(Next nothing is )([0-9]+)",data)
        if(len(found) > 0):
            nothingValue = found[0][1]
            cList.append(zFile.getinfo(nothingValue + ".txt").comment.decode("utf-8"))
        else:
            print("Finished:")
            print("".join(cList))
            break


chainFollow("90052")
os.remove("channel.zip")
