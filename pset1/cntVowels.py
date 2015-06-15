#Count vowels
s=raw_input(str("Enter a string:"))
cnt=0
for char in s:
    if char in 'aeiou':
        cnt = cnt +1
print('Number of vowels: '+str(cnt))