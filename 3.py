#!/usr/bin/python
from sys import argv
import re
import urllib.request as urllib

data = urllib.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
codec = data.info().get_param('charset','utf-8')
text = data.read().decode(codec).split("<!--")[1]
print("".join(re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]",text)))
