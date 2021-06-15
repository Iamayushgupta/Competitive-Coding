l=int(input())
u=int(input())
x=11
while len(str(x))!=len(str(u))+1:
    for i in range(1,10):
        z=x*i
        a=z**3
        k=str(a)[::-1]
        if l<=a and a<=u:
            if str(a)!=k:
                print(a,end='\t')
                print(z)
    x=int(str(x) + '1')