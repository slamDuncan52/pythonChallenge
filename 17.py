#!/usr/bin/python3
import re, bz2
import urllib.request as urllib
import xmlrpc.client
from urllib.parse import unquote_to_bytes

site = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
auth_handle = urllib.HTTPBasicAuthHandler()
auth_handle.add_password(realm='inflate',
         uri=site,
         user='huge',
         passwd='file')
urllib.install_opener(urllib.build_opener(auth_handle))

def chainFollow(nothingValue):
    seen = ''
    print("Working...")
    while True:
        response = urllib.urlopen(site+nothingValue)
        cookie = re.findall("(info=)(.*?)(;)",dict(response.info())["Set-Cookie"])
        data = str(response.read())
        found = re.findall("(next busynothing is )([0-9]+)",data)
        seen += cookie[0][1]
        if(len(found) > 0):
            nothingValue = found[0][1]
        else:
            print(bz2.decompress(unquote_to_bytes(seen.replace("+"," "))).decode())
            break
chainFollow("12345")
xmlMsngr = xmlrpc.client.ServerProxy("http://huge:file@www.pythonchallenge.com/pc/phonebook.php")
print(xmlMsngr.phone("Leopold"))
