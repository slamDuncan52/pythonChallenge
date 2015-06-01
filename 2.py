#!/usr/bin/python3
import re
import urllib.request as urllib

data = urllib.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")

codec = data.info().get_param("charset","utf-8")
text = data.read().decode(codec).split("<!--")[2]

print("".join(re.findall("[A-Za-z]",text)))
