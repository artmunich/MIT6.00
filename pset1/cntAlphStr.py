#Print the longest substring of s in which the letters occur in alphabetical order
#s='abcdefghijklmnopqrstuvwxyz'
s='dhnbvsrghra'

def strminus(s,substr):
    return s.replace(substr,'')

maxlen=0
for i in range(len(s)-1):
    for j in range(i,len(s)-1):
        if s[j]>s[j+1]:
            substr=s[i:j+1]
            print ('substr='+substr)
            if len(substr)>maxlen:
                maxlen=len(substr)
                maxstr=substr
            break
        elif (j==len(s)-2):
            substr=s[i:j+2]
            if len(substr)>maxlen:
                maxlen=len(substr)
                maxstr=substr
            break
print 'Longest substring in alphabetical order is: '+maxstr