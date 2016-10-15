__author__ = 'Anupam Panwar'

def main(setlist, totalsum, lengthofset):
    R = [[0 for i in range(totalsum+1)] for j in range(lengthofset+1)]
    for i in range(lengthofset+1):
        for j in range(totalsum+1):
            if i ==0 or j ==0:
                R[i][j] = 0
            elif setlist[i-1] <= j:
                R[i][j] = max(setlist[i-1]+ R[i][j-setlist[i-1]], R[i-1][j] )
            else:
                R[i][j] = R[i-1][j]
    #print R
    return R[lengthofset][totalsum]

test = int(raw_input().strip())
for i in range(test):
    lengthofset,totalsum=map(int,raw_input().split())
    setlist=map(int,raw_input().split())
    output = main(setlist, totalsum, lengthofset)
    print output



