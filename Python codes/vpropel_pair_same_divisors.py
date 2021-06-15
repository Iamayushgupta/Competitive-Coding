n=int(input())
def divisors(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    return count

count2=0  
for i in range(1,n+1):
    if n%i==0:
        x=int(n/i)
        print(i)
        print(x)
        a=divisors(i)
        print(a)
        b=divisors(x)
        print(b)
        if a==b:
            count2+=1
if n==1:
    print('-1')
else:
    print(int(count2/2))
        