import string
import re
import urllib2

frm = "abcdefghijklmnopqrstuvwxyz"
to = "cdefghijklmnopqrstuvwxyzab"
trans_table = string.maketrans(frm,to)

useUrl = "http://www.pythonchallenge.com/pc/def/map.html"
data = urllib2.urlopen(useUrl).read()

test = ""
for char in re.findall('<font color="#f000f0">(.+?)</tr>',data, re.DOTALL):
    test += char

print test.translate(trans_table)
print useUrl.translate(trans_table)
