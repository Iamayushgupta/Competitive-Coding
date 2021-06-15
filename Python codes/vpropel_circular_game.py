n=int(input())
l=[]
l_won=[]
for i in range(n):
    l.append(int(input()))
for i in range(n):
    if i==0:
        if l[n-1]<l[0] and l[0]<l[1]:
            l_won.append(i)
    if i==(n-1):
        if l[n-1]>l[n-2] and l[n-1]<l[0]:
            l_won.append(i)
    else:
        if l[i]<l[i+1] and l[i]>l[i-1]:
            l_won.append(i)
for i in l_won:
    print(i+1)
    
if len(l_won)==0:
    print('None')
        