#!/usr/bin/python3
import os
import urllib.request
import scipy.misc as misc
from PIL import Image, ImageDraw

print("It's romance stupid");

site = 'http://www.pythonchallenge.com/pc/return/mozart.gif'
auth_handle = urllib.request.HTTPBasicAuthHandler()
auth_handle.add_password(realm='inflate',
        uri=site,
        user='huge',
        passwd='file')
urllib.request.install_opener(urllib.request.build_opener(auth_handle))

data = urllib.request.urlopen(site)

with open('mozart.gif','wb') as imFile:
    imFile.write(data.read())

im = Image.new('RGB',(640,480));
im.paste(Image.open('mozart.gif'));
im.save('mozart.png');
imArr = misc.imread('mozart.png')
os.remove('mozart.gif')
os.remove('mozart.png')

draw = ImageDraw.Draw(im);

for line in range(0,len(imArr)):
    for col in range(0,len(imArr[line])):
        if((imArr[line][col] == [255,0,255]).all()):
            if((imArr[line][col] == imArr[line][col+4]).all()):
                drawLoc = 0
                for pixel in range(col,len(imArr[line])):
                   old = imArr[line][pixel]
                   draw.point((drawLoc,line),fill=(old[0],old[1],old[2]));
                   drawLoc = drawLoc + 1;
                for pixel in range(0,col):
                   old = imArr[line][pixel]
                   draw.point((drawLoc,line),fill=(old[0],old[1],old[2]));
                   drawLoc = drawLoc + 1;
                break;
im.show();
