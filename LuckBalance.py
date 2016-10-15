__Author__ = 'Anupam Panwar'

__Created_On__ = 9 / 25 / 2016

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]

def brick(ListA, ListB, n,k):
    totalsum =0
    importantcontest = []
    for i in range(len(ListA)):
        if (ListB[i]==0):
            totalsum +=ListA[i]
        else:
            importantcontest.append(ListA[i])
    a = list((sorted(importantcontest, reverse=True)[:k]))
    subList = [x for x in importantcontest if x not in a]
    sumSub = sum(subList)
    totalsum = totalsum + sum(a) - sumSub
    print totalsum


ListA = []
ListB = []
for a0 in xrange(n):
    a, b = raw_input().strip().split(' ')
    a,b = [int(a),int(b)]
    ListA.append(a)
    ListB.append(b)

brick(ListA,ListB, n,k)