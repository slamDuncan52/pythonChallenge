import re
import urllib2

def chainFollow(nothingValue):
    index = 0
    while 1:
        res = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+nothingValue)
        data = res.read()
        index = index + 1
        found = re.findall("(next nothing is )([0-9]+)",data)
        if(len(found) > 0):
            nothingValue = found[0][1]
            print str(index) + ": " + nothingValue
        elif(len(re.findall("(Divide)",data)) > 0):
            print "DIVIDE " + str(index) + ": " + nothingValue
            nothingValue = str(int(nothingValue)/2)
        else:
            print "FINISHED"
            break
chainFollow("12345")