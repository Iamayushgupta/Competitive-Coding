l=int(input())
u=int(input())
for i in range(l,u+1):
    for j in range(i,u+1):
        for k in range(j,u+1):
            if k**2 - j**2 - i**2==0:
                print(i,j,k,end=' ') 
                print('Exactly Pythagorean')
            elif k**2 - j**2 - i**2==1 or k**2 - j**2 - i**2==-1:
                print(i,j,k,end=' ')
                print('Very Close to Pythagorean')
            elif k**2 - j**2 - i**2==2 or k**2 - j**2 - i**2==-2:
                print(i,j,k,end=' ')
                print('Close to Pythagorean')