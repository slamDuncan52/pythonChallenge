#!/usr/bin/python2.7
import urllib2
import re
import bz2

data = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/integrity.html")
text =  data.read()
user = re.findall("un: '(.+)'\npw:",text)
pswd = re.findall("pw: '(.+)'\n-->",text)
newuser = bz2.decompress(user[0].decode('string_escape'))
newpswd = bz2.decompress(pswd[0].decode('string_escape'))
print newuser
print newpswd
