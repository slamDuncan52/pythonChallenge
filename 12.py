#!/usr/bin/python3
import os
import urllib.request
from PIL import Image, ImageDraw

site = "http://www.pythonchallenge.com/pc/return/evil2.gfx"
auth_handle = urllib.request.HTTPBasicAuthHandler()
auth_handle.add_password(realm="inflate",
                         uri=site,
                         user="huge",
                         passwd="file")
urllib.request.install_opener(urllib.request.build_opener(auth_handle))

data = urllib.request.urlopen(site)

text = data.read()
with open("first.jpg","wb") as imFile:
    imFile.write(text[0::5])
with open("second.png","wb") as imFile:
    imFile.write(text[1::5])
with open("third.gif","wb") as imFile:
    imFile.write(text[2::5])
with open("fourth.png","wb") as imFile:
    imFile.write(text[3::5])
with open("fifth.jpg","wb") as imFile:
    imFile.write(text[4::5])

first = Image.open("first.jpg")
second = Image.open("second.png")
third = Image.open("third.gif")
fourth = Image.open("fourth.png")
fifth = Image.open("fifth.jpg")

os.remove("first.jpg")
os.remove("second.png")
os.remove("third.gif")
os.remove("fourth.png")
os.remove("fifth.jpg")

first.show()
second.show()
third.show()
fourth.show()
fifth.show()
