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

imArr = misc.imread("wire.png")[0]
im = Image.new("RGB",(100,100))
os.remove("wire.png")

draw = ImageDraw.Draw(im)
point = 0
for vector in range(200,0,-1):
        dirn = (vector % 4)
        static = (vector // 4)
        for spot in range(0,(vector // 2)):
            spot = spot + (50-static)
            pixel = imArr[point]
            if(dirn % 2):
                x = 50 + (static * (dirn - 2))
                y = (dirn - 2) * spot + (99 * (dirn % 3))
            else:
                x = (dirn - 1) * -spot + (99 * (dirn // 2))
                y = 50 + (static * (dirn - 1))
            draw.point((x,y),fill=(pixel[0],pixel[1],pixel[2]))
            point = point + 1
im.show()
