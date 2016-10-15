#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())
p= s.count('a')
x = n/len(s)
print x*p + (s[:n%len(s)]).count('a')