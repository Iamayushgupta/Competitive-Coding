a=int(input())
b=int(input())
c=int(input())
n=int(input())
l=[]
for i in range(1,2*n,2):
    z=(-(a*i)-c)/b
    l.append(z)
for i in l:
    print(format(i,'0.2f'))