#!/usr/bin/python3
import os
import urllib.request
import scipy.misc as misc
from PIL import Image, ImageDraw

site = "http://www.pythonchallenge.com/pc/return/cave.jpg"
auth_handle = urllib.request.HTTPBasicAuthHandler()
auth_handle.add_password(realm="inflate",
        uri=site,
        user="huge",
        passwd="file")
urllib.request.install_opener(urllib.request.build_opener(auth_handle))

data = urllib.request.urlopen(site)

with open("cave.jpg","wb") as imFile:
    imFile.write(data.read())

imArr = misc.imread("cave.jpg")
im = Image.open("cave.jpg")
os.remove("cave.jpg")

draw = ImageDraw.Draw(im)
for row in range(0,len(imArr)):
    for col in range((row+1)%2,len(imArr[row]),2):
        draw.point((col,row),fill="black")
im.show()
