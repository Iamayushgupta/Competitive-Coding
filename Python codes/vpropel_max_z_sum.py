r=int(input())
c=int(input())
l=[]
for i in range(r):
    z=list(map(int,input().split()))
    l.append(z)
sum_list=[]
for i in range(c-1):
    for j in range(r-1):
        sum_list.append(l[i][j]+l[i+1][j]+l[i][j+1]+l[i+1][j+1])
        
mx=max(sum_list)
print(mx)

for i in range(c-1):
    for j in range(r-1):
        if (l[i][j]+l[i+1][j]+l[i][j+1]+l[i+1][j+1])==mx:
            print(i+1,"\t",j+1)
            print(l[i][j],"\t",l[i][j+1],"\t",l[i+1][j],"\t",l[i+1][j+1])
        
        


        
    