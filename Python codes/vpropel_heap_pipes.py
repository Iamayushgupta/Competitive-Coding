import heapq as heap
n=int(input())
list1=[]
for i in range(n):
    x=int(input())
    heap.heappush(list1,x)

z=0
while True:
    if len(list1)>1:
        y=heap.heappop(list1)
        x=heap.heappop(list1)
        p=x+y
        z+=p
        heap.heappush(list1,p)
    else:
        break

if z==0:
    print(z+x)
    
else:
    print(z)


