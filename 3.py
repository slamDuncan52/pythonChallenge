from sys import argv
import re
import urllib2

data = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read()

test = data.split("<!--")

answer = ""
for char in  re.findall("[A-Za-z]",test[2]):
    answer += char
print answer
