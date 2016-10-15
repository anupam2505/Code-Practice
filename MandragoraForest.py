##__Author__ = 'Anupam Panwar'

##__Created_On__ = 9 / 25 / 2016

t = int(raw_input().strip())


def mandragora(n,a):

    a = sorted(a)
    S=1
    ## Dynamic programming here. saving the same instead of sum for each iteration
    for i in xrange(1,n):
        a[i] += a[i-1]
    maximum_experience = a[n-1]
    for i in range(0, len(a)):
        S+=1
        maximum_experience = max(maximum_experience, S*(a[n-1]-a[i]))
    print maximum_experience


for a0 in xrange(t):
    n = int(raw_input().strip())
    a = map(int,raw_input().strip().split(' '))
    mandragora(n,a)