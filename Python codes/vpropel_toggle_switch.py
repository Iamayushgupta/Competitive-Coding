n=int(input())
m=int(input())
bool=True
for i in range(1,m+1):
    if m%i==0:
        bool=not bool
if bool:
    print('Off')
else:
    print('On')
    
        