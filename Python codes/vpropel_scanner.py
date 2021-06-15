l1=list(map(float,input().split()))
n=int(input())
bool=True
l2=[]
sum=0
for ele in l1:
    if ele>=0.2 and ele<=0.7:
        l2.append(0)
    elif ele>=0.71 and ele<=1.2:
        l2.append(1)
    elif ele>=1.21 and ele<=1.7:
        l2.append(2)
    elif ele>=1.71 and ele<=2.2:
        l2.append(3)  
    elif ele>=2.21 and ele<=2.7:
        l2.append(4)
    elif ele>=2.71 and ele<=3.2:
        l2.append(5)
    elif ele>=3.21 and ele<=3.7:
        l2.append(6)
    elif ele>=3.71 and ele<=4.2:
        l2.append(7)
    elif ele>=4.21 and ele<=4.7:
        l2.append(8)
    elif ele>=4.71 and ele<=5.2:
        l2.append(9)
        
for i in l2:
    if bool:
        sum+=i*1
        bool=not bool
    else:
        sum+=i*3
        bool=not bool
if sum%10==n:
    print('Yes')
else:
    print('No')
        