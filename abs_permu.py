__author__ = 'Anupam Panwar'

#!/bin/python

import sys
def main(n,k):
    A = [i for i in range(1,n+1)]
    if (k==0):
        return A
    if (n%(2*k))!=0:
        return [-1]
    i=0
    while (i<n-k):
        if (i+1%k)==0:
            i +=k
        else:
            A[i], A[i+k] = A[i+k], A[i]

    return A

t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    A = main(n,k)
    print ' '.join(str(x) for x in A)




