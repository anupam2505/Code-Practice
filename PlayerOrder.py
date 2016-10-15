

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
    ind =0
    if (len(mat)==0):
        return list
    if (len(mat)==1):
        list.append(mat[0][0])
        return list
    maximum =0
    for i in range(len(mat)):
        flag = True


        pointer =0
        for j in range(1, n):

            if (mat[i][j]=='W'):
                pointer+=1
        if (maximum<pointer):
            maximum =  pointer
            ind =i
    list.append(mat[ind][0])
    del mat[ind]
    list = matrix(mat, n-1, list)
    return list

a = matrix (mat,n, list)
print a