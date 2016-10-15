#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
s = raw_input().strip()
friends = map(int,raw_input().strip().split(' '))

def check(n,s, friends):
    for i in range(n):
        if (i+1) in friends:
            if (s[i]=='0'):
                print "YES"
                return
    print "NO"
    return

check(n,s, friends)