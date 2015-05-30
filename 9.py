#!/usr/bin/python
import urllib.request
import re
site = "http://www.pythonchallenge.com/pc/return/good.html"
auth_handle = urllib.request.HTTPBasicAuthHandler()
auth_handle.add_password(realm="inflate",
                        uri=site,
                        user="huge",
                        passwd="file")
urllib.request.install_opener(urllib.request.build_opener(auth_handle))

data = urllib.request.urlopen(site)
codec = data.info().get_param("charset","utf-8")
text = data.read().decode(codec)
firstStr = re.findall("first:\n(.+)second:",text,re.DOTALL)
secondStr = re.findall("second:\n(.+)-->",text,re.DOTALL)
firstNums = []
secondNums = []
for num in firstStr[0].split(','):
    firstNums.append(int(num))
for num in secondStr[0].split(','):
    secondNums.append(int(num))

sumNum = []
for item in range(0,len(secondNums)-1):
    sumNum.append( firstNums[item] + secondNums[item])
print(sumNum)
