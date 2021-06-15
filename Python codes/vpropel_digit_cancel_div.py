x=int(input())
y=int(input())
if(y==0):
    print("-1.00")
    exit()
s1=str(x)
s2=str(y)
s1=list(s1)
s2=list(s2)
f1=[]
f2=[]
for i in s1:
    if i in s2:
        s1.remove(i)
        s2.remove(i)
for i in s1:
    if i in s2:
        s1.remove(i)
        s2.remove(i)
        
if(len(s1)==0):
    s1.append('1')
if(len(s2)==0):
    s2.append('1')
x1=''.join(s1)
x2=''.join(s2)

x1=int(x1)

x2=int(x2)
if(x2==0):
    print("-1.00")
    exit()
else:
    div=x1/x2
    
    print(format(div,".2f"))