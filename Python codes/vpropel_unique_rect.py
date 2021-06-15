n=int(input())
l=[]
temp=0
for i in range(1,n+1):
    if n%i==0:
        x=int(n/i)
        if i!=temp:
            l.append(i)
            temp=x
        else:
            break
print(len(l))
for i in range(1,n+1):
    if n%i==0:
        x=int(n/i)
        if i!=temp:
            print(i,x)
            temp=x
        else:
            break
        