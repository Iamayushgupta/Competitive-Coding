n=int(input())
m=int(input())
x=int(n*m)
a=list(str(n))
b=list(str(m))
c=list(str(x))
result=a+b+c

bool = "Yes"

for i in range(1,10):
    if result.count(i)!=1:
        bool = "No"

print(bool)