__author__ = 'Anupam Panwar'

m,n=map(int,raw_input().split())
listm=map(int,raw_input().split())
listn=map(int,raw_input().split())

R = [[0 for i in range(n+1)] for j in range(m+1)]

def LCS(listm,listn, m, n, R):
    for i in range(m):
        for j in range(n):
            if (i==0 or j==0):
                result =0;
            elif (listm[i]==listn[j]):
                result = 1 + R[i-1][j-1]
            else:
                result = max(R[i-1][j], R[i][j-1])
            R[i][j] = result

LCS(listm,listn, m-1, n-1, R)

print R
i, j = m-1, n-1
list = []
while (i>= 0 and j >= 0):
    if listm[i] == listn[j]:
        list.append(listm[i])
        j -=1
        i-=1
    else:
        if R[i][j-1]>R[i-1][j]:
            j-=1
        else:
            i-=1

#list.append(listm[i])
list = map(str, reversed(list))
print ' '.join(list)



