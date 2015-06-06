#!/usr/bin/python3
import os
import urllib.request
import xmlrpc.client

site = "www.pythonchallenge.com/pc/phonebook.php"
auth_handle = urllib.request.HTTPBasicAuthHandler()
auth_handle.add_password(realm="inflate",
        uri="http://"+site,
        user="huge",
        passwd="file")
urllib.request.install_opener(urllib.request.build_opener(auth_handle))

xmlMsngr = xmlrpc.client.ServerProxy("http://huge:file@"+site)

print(xmlMsngr.phone('Bert'))
print("italy is the answer")
