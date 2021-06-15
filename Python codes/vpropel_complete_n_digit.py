n=int(input(''))
m=int(input(''))
bool=True

for i in range(2,m+1):
    
    for j in range(10**(n-1),10**(n)):
        result=int(str(j) + str(j))
        if result%i==0:
            if (j == (10**n)-1):
                print(i)
                bool=False
        else:
            break
            
if bool:
    print('No complete factors')
    
    