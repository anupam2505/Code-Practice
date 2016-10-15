__author__ = 'Anupam Panwar'

mn = raw_input().strip()
t = int(mn.split(" ")[0])
t1 = int(mn.split(" ")[1])

best =0

R = [[-1 for i in range(t1)] for j in range(t1)]

def main( R, t,t1, best):
    for i in range(t):
        row = raw_input().strip()
        Matrix = [0 for i in range(t1)]
        for x in range(t1):
            if (row[x] =='.'):
                Matrix[x] = 1
        for j in range(t1):
            visible =1
            for k in range(j+1,t1,1):
                if Matrix[k] ==0:
                    visible =0
                if (Matrix[j]==1 and Matrix[k] ==1):
                    if (R[j][k] >= 0):
                         R[j][k] += 1
                    if (R[j][k] <0 and visible ==1):
                        R[j][k] =0
                    if (R[j][k] > 0 and visible ==1):
                        v = 2*R[j][k] +2*(k-j)
                        if (v > best):
                            best=v
                else:
                    R[j][k]=-1
    if best >0:
        print best
    else:
        print "impossible"

main(R,t,t1, best)
