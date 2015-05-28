from sys import argv
import re
import urllib2

data = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().split("<!--")

print "".join(re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]",data[1]))
