__Author__ = 'Anupam Panwar'

__Created_On__ = 9 / 26 / 2016

s = list(str(raw_input()))
i=1
counter =1
end =0
totalnumber =1
while(i<len(s)):
   character = s[0]
   if (s[i]!=character):
       i +=1
       counter +=1
   else:
       if (s[:counter]== s[counter:2*counter]):
            end =counter
            totalnumber +=1
            break
       else:
           i +=1
           counter +=1


s = ''.join(s)
a = ''.join(s[:end])
print s.count(a)
print ''.join(s[:end])