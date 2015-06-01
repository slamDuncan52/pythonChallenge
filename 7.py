#!/usr/bin/python3
import urllib.request as urllib
import re
import os
import scipy.misc as misc
from scipy.stats import mode as mode

data = urllib.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")
with open("oxygen.png","wb") as imFile:
    imFile.write(data.read())

imArr = misc.imread("oxygen.png")
os.remove("oxygen.png")

penult = ""
mid = len(imArr)/2
blkEnd = 0

for pixel in imArr[mid]:
    if(pixel[0] != pixel[1]):
        break
    blkEnd += 1

cur = 0
prev = 0
tmpSize = 1
blkSize = 1
blkList = []

for col in range(0,blkEnd):
    cur = imArr[mid][col][0]
    if(cur == prev):
        tmpSize += 1
    else:
        blkList.append(tmpSize)
        tmpSize = 1
        prev = cur

blkSize = int(mode(blkList)[0][0])

for col in range(0,blkEnd,blkSize):
    penult +=chr(imArr[mid][col][0])
print(penult)

finalArr = []
for num in re.findall("([0-9]+)",penult):
    finalArr.append(chr(int(num)))
print ("".join(finalArr))
