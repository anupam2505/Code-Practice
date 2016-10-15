#!/bin/python3

import sys


n = int(raw_input().strip())
s = str(raw_input().strip())
unichar = list(set(s))



def character(s,unichar):
    if (len(s)>1000):
        print 0
        return
    for c in s:
        if not c.islower():
         print 0
         return

    maximum=0
    for i in range(len(unichar)-1):
        for j in range(i+1,len(unichar)):
            subset = [unichar[i],unichar[j]]
            delset = [x for x in unichar if x not in subset]
            flag = True
            snew = s
            for k in delset:
                snew = snew.replace(k,'')
            for i in range(len(snew)-1):
                if snew[i] == snew[i+1]:
                    flag = False
                    break
            if (flag==True):
                maximum = max(maximum,len(snew))
    print maximum



character(s,unichar)


