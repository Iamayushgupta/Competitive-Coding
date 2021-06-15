n=int(input())
l=[]
for i in range(n):
    x=input()
    z=len(x)
    l.append(x)
x=input()
a=''
for i in range(z):
    a+=x[int(input())-1]
if a in l:
    print('Valid')
else:
    print('Invalid')