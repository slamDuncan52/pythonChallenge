import urllib.request as urllib
import re

frm = "abcdefghijklmnopqrstuvwxyz"
to = "cdefghijklmnopqrstuvwxyzab"
trans_table = str.maketrans(frm,to)

useUrl = "http://www.pythonchallenge.com/pc/def/map.html"
data = urllib.urlopen(useUrl)
codec = data.info().get_param("charset","utf-8")
text = data.read().decode(codec)

test = "".join(re.findall('<font color="#f000f0">(.+?)</tr>',text, re.DOTALL))

print(test.translate(trans_table))
print(useUrl.translate(trans_table))
