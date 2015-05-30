#!/usr/bin/python
import pickle
import urllib.request as urllib
res = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = res.read()
decode = pickle.loads(data)
for item in decode:
    answer = ""
    for pair in item:
        answer += pair[0] * pair[1]
    print(answer)
