
maxi = []
mini = []

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
if (k>n):
    k =n

for i in range(n):
    cost = map(int,raw_input().strip().split(' '))
    maxi.append(cost[0])
    mini.append(cost[1])

wash = []
notwash = []

ind = []
maxi1 = list(maxi)

for i in range(k):
    maximumindex = maxi.index(max(maxi))
    maxi[maximumindex] =0
    ind.append(maximumindex)

for j in range(n):
    if (j in ind):
        wash.append(maxi1[j])


minind =[]
for i in range(n):
    if (i not in ind):
        minind.append(i)

for j in range(n):
    if (j in minind):
        notwash.append(mini[j])


if ((sum(wash)- sum(notwash))<0):
    print str(0)
else:
    print str(sum(wash)- sum(notwash))
