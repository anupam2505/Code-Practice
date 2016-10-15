__Author__ = "Anupam Panwar"

__Date__ = 10 / 2 / 16

def countduplicates(array):
    counter =0
    hash =dict()
    for x in array:
        if x in hash and hash[x] ==1:
            counter+=1
        elif x in hash:
            hash[x] +=1
        else:
            hash[x]= 1
    print counter

array = list()

n = int(raw_input().strip())
for a0 in xrange(n):
    k = int(raw_input().strip())
    array.append(k)
countduplicates(array)


