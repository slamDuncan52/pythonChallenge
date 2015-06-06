#!/usr/bin/python3
import urllib.request
import re
import os
from PIL import Image, ImageDraw
site = "http://www.pythonchallenge.com/pc/return/good.html"
auth_handle = urllib.request.HTTPBasicAuthHandler()
auth_handle.add_password(realm="inflate",
        uri=site,
        user="huge",
        passwd="file")
urllib.request.install_opener(urllib.request.build_opener(auth_handle))

data = urllib.request.urlopen(site)

codec = data.info().get_param("charset","utf-8")
text = data.read().decode(codec)

firstStr = re.findall("first:\n(.+)second:",text,re.DOTALL)
secondStr = re.findall("second:\n(.+)-->",text,re.DOTALL)

firstNums = []

for num in firstStr[0].split(','):
    firstNums.append(int(num))
for num in secondStr[0].split(','):
    firstNums.append(int(num))

firstNums = list(zip(firstNums[0::2],firstNums[1::2]))

im = Image.new("RGB",(500,500),"black")
draw = ImageDraw.Draw(im)

draw.point(firstNums)
im.show()


print("(It's a bull okay)")
