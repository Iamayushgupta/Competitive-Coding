n=int(input())
line=input().split()
l=[]
for i in range(n):
    l.append(int(line[i]))

z=0
p=int(l.count(1))
q=int(l.count(2))
r=int(l.count(3))
s=int(l.count(4))
z+=s
if r>=p:
    z+=r
    if q%2==0:
        z+=(q/2)
    elif q==1:
        z+=1
    else:
        z+=(q//2) + 1

else:
    z+=r
    y=p-r
    a=y%4
    b=y//4
    if q%2==0:
        z+=(q/2)
        if a==0:
            z+=b
        else:
            z+=b+1
    else:
        z+=(q//2)
        if a>2:
            z+=b+2
        else:
            z+=b+1
    
print(z)


