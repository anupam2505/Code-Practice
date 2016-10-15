__Author__ = "Anupam Panwar"

__Date__ = 9 / 30 / 16

n,p,q = raw_input().strip().split(' ')
n,p,q = [int(n),int(p), int(q)]


def printseq(n,p,q):
    out = list()
    for i in range(1,n+1):
        digits = set([int(x) for x in str(i)])
        if (i%p ==0 or i%q ==0) and (p in digits or q in digits):
            out.append("OUTTHINK")

        elif (p in digits or q in digits):
            out.append("THINK")
        elif (i%p ==0 or i%q ==0):
            out.append("OUT")
        else:
            out.append(str(i))
    print ','.join(map(str, out))

printseq(n,p,q)
