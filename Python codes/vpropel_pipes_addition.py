n=int(input())
list1=[]
for i in range(n):
    x=int(input())
    list1.append(x)

z=0
while True:
    if len(list1)>1:
        list1.sort()
        y=list1[0] + list1[1]
        z+=y
        del list1[0]
        del list1[0]
        list1.append(y)
    else:
        break

if z==0:
    print(z+x)
    
else:
    print(z)

