n=int(input())
l=len(str(n))
bool = True
for i in range(l):
    if int(str(n)[:i+1])%l!=0:
        print('No')
        bool= not bool
        break
    else:
        l=l-1

if bool:
    print('Yes')
        
