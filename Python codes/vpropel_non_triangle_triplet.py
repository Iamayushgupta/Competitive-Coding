n=int(input())
list1=[]
for i in range(1,n):
    for j in range(i,n):
        c=n-i-j
        if c<j:
            break
        if c>=i+j:
            list1.append((i,j,c))
print(len(list1))