import math
n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

def summing(c):
    n = len(c)
    if (n ==1):
        return c[0]

    res = sum(c) * n
    for i in range(n):
        res +=summing(c[:n])
        res+=summing(c[i+1:])
    print res%(math.pow(10,9)+7)

summing(c)