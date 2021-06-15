n=int(input())
a=int(input())
b=int(input())
l=[]
for i in range(n+1):
    x=a*i
    y=b*(n-i)
    l.append(max(x,y))
    
print(min(l))