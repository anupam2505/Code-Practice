__Author__ = 'Anupam Panwar'

__Created_On__ = 9 / 26 / 2016



n = int (raw_input())
mat = []

for a0 in xrange(n):
    S = list(str(raw_input()))
    mat.append([])
    mat[a0].append(a0+1)
    for i in S:
        mat[a0].append(i)


list = []
def matrix(mat,n, list):
   counter,i=0,0
   while (counter<n):
      for j in range(n):
          flag = False
          if (mat[i][j]=='W'):
              list.append(i+1)
              i =j
              flag = True
              counter +=1
              break
          if flag == False:
              i +=1

a = matrix (mat,n, list)
print a