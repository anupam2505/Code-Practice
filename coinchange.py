# Enter your code here. Read input from STDIN. Print output to STDOUT

__Author__ = 'Anupam Panwar'

__Created_On__ = 9 / 25 / 2016

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
S = map(int,raw_input().strip().split(' '))



def count(S, n, m):
    mat = [[0 for i in range(m)] for j in range(n+1)]
    for j in range(m):
        mat[0][j]=1

    for i in range(m):
        for j in range(1,n+1):
            if j-S[i]>=0:
                a = S[i]
                x = mat[j-S[i]][i]
            else:
                x=0
            
            if (i>0):
                y = mat[j][i-1]
            else:
                y=0
            mat[j][i]=x+y
    
    print mat[n][m-1]

count (S,n,m)