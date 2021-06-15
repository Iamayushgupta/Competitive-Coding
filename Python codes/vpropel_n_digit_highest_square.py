import math 
n=input()
m=len(n)
x=(pow(math.ceil(math.sqrt(pow(10, m))) - 1, 2))

bool=True

while bool: 
    if len(set(str(x))) !=len(str(x)):
        x=int(math.sqrt(x) - 1)**2
    else:
        bool = not bool

for i in range(0,m):
    print(n[i] +  ' ' + str(x)[i])