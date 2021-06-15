n=int(input())
m=int(input())
list1=[]
list2=[]
for i in range(2,n):
    if n%i==0:
        list1.append(i)
for i in range(2,m):
    if m%i==0:
        list2.append(i)
x=sum(list1)
y=sum(list2)
if x>y:
    print(n)
elif y>x:
    print(m)
else:
    print('No dominance')
    