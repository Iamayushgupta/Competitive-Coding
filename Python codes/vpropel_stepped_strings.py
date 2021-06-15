import re
s1=input()
s2=input()
x=s1.index(' ') 
y=s2.index(' ')
def func(String):
    x=len(String)
    d=ord(String[1])-ord(String[0])
    for i in range(2,x):
        if (ord(String[i])-ord(String[i-1]))!=d:
            return False

a=func(s1.split()[0])
b=func(s1.split()[1])
c=func(s2.split()[0])
d=func(s2.split()[1])

res1 = bool(re.match('[a-zA-Z\s]+$',s1))
res2 = bool(re.match('[a-zA-Z\s]+$',s2))
if x!=y:
    print('Strings differ in space')
elif len(s1)!=len(s2):
    print('Length different')
elif res1==False or res2==False:
    print('Strings contain non alphabets')
elif a==False or b==False or c==False or d==False:
    print('Strings are not stepped')
else:
    print('Strings are stepped')

