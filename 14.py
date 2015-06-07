#!/usr/bin/python3
import os
import urllib.request
import scipy.misc as misc
from PIL import Image, ImageDraw

site = "http://www.pythonchallenge.com/pc/return/wire.png"
auth_handle = urllib.request.HTTPBasicAuthHandler()
auth_handle.add_password(realm="inflate",
        uri=site,
        user="huge",
        passwd="file")
urllib.request.install_opener(urllib.request.build_opener(auth_handle))

data = urllib.request.urlopen(site)

with open("wire.png","wb") as imFile:
    imFile.write(data.read())

imArr = misc.imread("wire.png")
im = Image.new("RGB",(100,100))
os.remove("wire.png")

draw = ImageDraw.Draw(im)
point = 0
square = 0
#0 is right
#1 is up
#2 is left
#3 is down
for vector in range(200,0,-1):
        direction = (vector % 4)
        yVec = (vector // 4)
        for spot in range(0,(vector // 2)):
            spot = (spot + square)
            if(direction == 0):
                draw.point((spot,50-yVec),fill=(imArr[0][point][0],imArr[0][point][1],imArr[0][point][2]))
            elif(direction == 1):
                draw.point((50-yVec,99-spot),fill=(imArr[0][point][0],imArr[0][point][1],imArr[0][point][2]))
            elif(direction == 2):
                draw.point((99-spot,50+yVec),fill=(imArr[0][point][0],imArr[0][point][1],imArr[0][point][2]))
            elif(direction == 3):
                draw.point((50+yVec,spot),fill=(imArr[0][point][0],imArr[0][point][1],imArr[0][point][2]))
            point = point + 1
        if(direction == 1):
            square = square + 1
im.show()
