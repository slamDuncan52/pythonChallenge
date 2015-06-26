#!/usr/bin/python3
import re
import urllib.request as urllib
import http.cookiejar

site = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
cookieJar = http.cookiejar.CookieJar()
urllib.install_opener(urllib.build_opener(urllib.HTTPCookieProcessor(cookieJar)))
def chainFollow(nothingValue):
    index = 0
    seen = []
    print("Working...")
    while 1:
        with urllib.urlopen(site+nothingValue) as response:
            data = response.read()
            codec = response.info().get_param('charset','utf-8')
            data = data.decode(codec)
            for cookie in cookieJar:
                print(cookie.value)
        index = index + 1
        found = re.findall("(next busynothing is )([0-9]+)",data)
        if(len(found) > 0):
            nothingValue = found[0][1]
            print(str(index) + ": " + nothingValue)
            if(nothingValue in seen):
                break
            else:
                seen.append(nothingValue)
        else:
            print("Finished: "+ data)
            break
chainFollow("6711")
