#!/usr/bin/python3
def compNext(oldSeq):
    curDigit = oldSeq[0]
    count = 0
    newSeq = []
    for num in oldSeq:
        if(num == curDigit):
            count += 1
        else:
            newSeq.append(count)
            newSeq.append(curDigit)
            curDigit = num
            count = 1
    newSeq.append(count)
    newSeq.append(curDigit)
    return newSeq

a = [[1]]

for i in range(0,31):
    a.append(compNext(a[i]))
    
print("len(a[30])=" + str(len(a[30])))
