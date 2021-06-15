k=int(input())
m=int(input())
l=list(map(int,input().split()))
x=list(set(l))              
l.sort(reverse=True)
temp=l.copy()
list1=[]

for i in x:
    list1.append(i)

for i in x:
    if l.count(i)>i+1:
        list1.append(i)
        for _ in range(i+1):
            temp.pop(i)

z=0
while len(list1)!=k:
    list1.append(temp[z])
    z+=1
            
print(sum(list1)+k)
    
    
    
    
