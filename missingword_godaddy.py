__Author__ = "Anupam Panwar"

__Date__ = 10 / 2 / 16

s = "I am using hackerrank to improve programming am"
t = "am hackerrank to improve"


def  missingWords(s, t):
    slist = s.split(" ")
    finallist = list()
    tlist = t.split(" ")
    slength = len(slist)
    tlength = len(tlist)
    i,j=0,0
    for i in xrange(tlength):
        for j in xrange(slength):
            if (slist[j] ==tlist[i]):
                finallist.append(j)
                break

    returnlist = [i for j, i in enumerate(slist) if j not in finallist]
    return returnlist


for i in (missingWords(s,t)):
    print i
