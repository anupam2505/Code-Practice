import re

s = "IBM cognitive computing|IBM 'cognitive' computing is a revolution| ibm cognitive  computing|'IBM Cognitive Computing' is a revolution?"
s1 = "'Computer Science Department'|Computer-Science-Department|the 'computer science department'"


c = s1.strip().split('|')
c = sorted(c)
dupl = list(c)
#c = raw_input().strip().split('|')
for i in range(len(dupl)):
        s = dupl[i].lower()
        s= s.rstrip().lstrip()
        s = re.sub('[^a-zA-Z\d\s]', '', s)
        s = ' '.join(s.split())
        dupl[i] =s
indices = list()

for i in range(len(dupl)):
    for j in range(i+1,len(dupl)):
        if (dupl[i] in dupl[j]):
            indices.append(i)
            break
        elif (dupl[j] in dupl[i]):
            indices.append(j)
            break

indices = set(list(indices))

somelist = [i for j, i in enumerate(c) if j not in indices]
print '|'.join(somelist)



