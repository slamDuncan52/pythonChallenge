import urllib.request as urllib
import re
import bz2

data = urllib.urlopen("http://www.pythonchallenge.com/pc/def/integrity.html")
codec = data.info().get_param("charset","unicode_escape")
text =  data.read().decode(codec)
user = re.findall("un: '(.+)'\npw:",text)[0]
pswd = re.findall("pw: '(.+)'\n-->",text)[0]
print(bytes(user, "utf-8"))
print(bytes(pswd, "utf-8"))


garbage = b'BZh91AY&SYA\xc2\xaf\xc2\x82\r\x00\x00\x01\x01\xc2\x80\x02\xc3\x80\x02\x00 \x00!\xc2\x9ah3M\x07<]\xc3\x89\x14\xc3\xa1BA\x06\xc2\xbe\x084'
trash = b'BZh91AY&SY\xc2\x94$|\x0e\x00\x00\x00\xc2\x81\x00\x03$ \x00!\xc2\x9ah3M\x13<]\xc3\x89\x14\xc3\xa1BBP\xc2\x91\xc3\xb08'

print(bz2.decompress(garbage))
print(bz2.decompress(trash))
