


s = str(raw_input().strip())

def findpowerset(string):
    set = [1<<j for j in xrange(len(string))]
    for i in xrange(1, 2**(len(string))):
        yield "".join([str(string[j]) for j in range(n) if (set[j] & i)])



def buildSubsequences( s):
    return sorted((list(set(findpowerset(s)))))
