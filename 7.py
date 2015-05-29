import urllib2
import re
import os
from scipy import misc

data = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")
with open("oxygen.png","wb") as imFile:
    imFile.write(data.read())

imArr = misc.imread("oxygen.png")

penult = ""
prev = " "

for i in range(0,608,7):
    penult +=chr(imArr[47][i][0])
print penult

finalArr = []
for thing in re.findall("([0-9]+)",penult):
    finalArr.append(chr(int(thing)))
print "".join(finalArr)
os.remove("oxygen.png")
