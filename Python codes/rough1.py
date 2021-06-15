n=int(input())
l=list(map(int,input().split()))
x=sorted(l)
def hw(lis,new,n):
    count=0
    for i in range(n):
        if lis[i]!=new[i]:
            a=new[i]
            b=lis.index(a)
            lis[i] , lis[b] = lis[b] , lis[i]
            count+=1
    return count
print(min(hw(l,x,n),hw(l,x[::-1],n)))
