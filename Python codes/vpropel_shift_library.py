n=int(input())
bool=True
sum=0
x=1
while sum<=n:
    sum+=3*x
    x+=1

a=1
r=0
s=0
sum1=0
while sum1<n:
    if bool:
        if (sum1+a)<=n:
            r+=a
            sum1+=a
            if sum1+(a*2) <=n:
                s+= a*2
                sum1+=a*2
            else:
                s+= (n-sum1)
                temp=0
                break
        else:
            r+= (n-sum1)
            temp=1
            break
        bool =  not bool
    else:
        if sum1+ (2*a)<=n:
            r+=2*a
            sum1+=2*a
            if (sum1 + a)<=n:
                s+=a
                sum1+=a
            else:
                s+=n-sum1
                temp=0
                break
        else:
            r+=n-sum1
            temp=1
            break
        bool= not bool
    a+=1
print(x-1)
print(r,end='\t')
print(s)
if temp==0:
    print('Somu')
else:
    print('Ramu')

                
        
        

    