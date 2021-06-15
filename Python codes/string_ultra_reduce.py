s=input()
def reduce(s):
    new=''
    for i in range(0,len(s)):
        if i==0: 
            if s[i]!=s[i+1]:
                new+=s[i]
        elif i==len(s)-1:
            if s[i]!=s[i-1]:
                new+=s[i]
        elif s[i+1]!=s[i] and s[i]!=s[i-1]:
            new+=s[i]
    return new
while True:
    if len(reduce(s))==0:
        print("Empty String")
        exit()
    else:
        if s==reduce(s):
            break
        s=reduce(s)
         
print(s)