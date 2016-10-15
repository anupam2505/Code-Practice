#!/bin/python3

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

def pair(n,c):
    c = sorted(c)
    i=0
    total =0
    while (i<n-1):
        if (c[i]==c[i+1]):
            total +=1
            i+=2
        else:
            i+=1
    print total

pair(n,c)


