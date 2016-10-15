# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

t = int(raw_input().strip())

input_list = list()
for a0 in xrange(t):
    t = int(raw_input().strip())
    input_list.append(t)

def check_winner_list(input_list):
    for i in input_list :
        check_winner(i, 0)

def check_winner (i,j):
    if (i==1):
        if (j%2==0):
            print "Richard"
        else:
            print "Louise"
    else :
        k = power_two(i)
        if (2**k == i):
            i = i/2
            j = j+1
            check_winner(i,j)
        else:
            i = i - 2**k
            j = j+1
            check_winner(i,j)

def power_two(n):
    return int(math.log(n, 2))

check_winner_list(input_list)