#list all alphabetical ordered substrings
s='abzghicbat'

def strminus(s,substr):
    return s.replace(substr,'')


for i in range(len(s)-1):
    if s[i]>s[i+1]:
        substr=s[:i+1]
        print substr
        s=strminus(s,substr)