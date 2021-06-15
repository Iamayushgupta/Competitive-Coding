num=int(input())

def fact(n):
    x=1
    if n%2==0:
        for j in range(2,n+1,2):
            x=x*j
    else:
        for j in range(1,n+1,2):
            x=x*j
    return x
def isfact(n):
    i = 1
    while(True) : 
        if (n % i == 0):
            z=n 
            n=n/i 
        else: 
            break 
        i += 1
    if (n == 1) : 
        return fact(int(z))
    else : 
        return -1
print(isfact(num))