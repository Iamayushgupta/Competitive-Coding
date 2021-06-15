n=int(input())
s1=''
s2=''
for i in range(n):
    s1+=input()
for i in range(n):
    s2+=input()
    
a=s2.index(s1[0])
b=s2[a:] + s2[:a]
if b==s1:
    print('Not Shuffled')
else:
    print('Shuffled')
