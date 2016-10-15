#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
c = map(int,raw_input().strip().split(' '))

maxi =[]
count =0
for i in range(n):
    if i in c:
       maxi.append(count)
       count =0
    else:
        count +=1
maxi.append(count)

if (len(maxi) <=2):
    print max(maxi)
else:
    maximum = max(maxi[1:len(maxi)-1])
    maximum1 = maxi[0]
    maximum2 = maxi[len(maxi)-1]
    maximum3  = (maximum+1)/2

    print max(maximum1,maximum2,maximum3)

