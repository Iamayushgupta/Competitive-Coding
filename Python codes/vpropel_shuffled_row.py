n=int(input())
m=int(input())
bool=True
l=[]
for i in range(n):
    x=list(map(int,input().split()))
    x.sort()
    l.append(x)
for i in range(n-1):
    if l[i]!=l[i+1]:
        print('Not Shuffled Row Matrix')
        bool= not bool
        break
if bool:
    print('Shuffled Row Matrix')
