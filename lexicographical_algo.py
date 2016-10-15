__author__ = 'Anupam Panwar'

def main(ascii):
    length = len(ascii)
    w = length-1
    while(w>0 and ascii[w]<=ascii[w-1]):
        w -=1
    if w<=0:
        print "no answer"
        return

    x = length -1
    while(x >=w):
        if ascii[x]> ascii[w-1]:
            ascii[x], ascii[w-1] = ascii[w-1], ascii[x]
            break
        x -=1

    ascii[w:] = ascii[length-1: w-1:-1]
    out = ''.join(map(chr,ascii))
    print out
    return


test = int(raw_input().strip())

for i in range(test):
    sentence = raw_input().strip()
    sentence = list(sentence)
    ascii = [ord(c) for c in sentence]
    a = main(ascii)



