n=int(input())
list1=[]
for i in range(0,n):
    i=int(input())
    list1.append(i)
average=[]
x=0
for j in range(0,n):
    x+=list1[j]
    y=x/(j+1)
    q=round(y,2)
    average.append(q)
        
p=(sum(average)/n)
print('%.2f'%p)
