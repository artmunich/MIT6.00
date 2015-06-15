#counting bobs
str1=str(raw_input('Input a string of lower case characters:'))
N=len(str1)
cnt=0
for i in range(N-2):
    str2=str1[i:i+3]
    if str2=='bob':
        cnt=cnt+1
print('Number of times bob occurs is: '+str(cnt))
