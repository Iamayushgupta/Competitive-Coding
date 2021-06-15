import math
x=int(input(''))

a = 1
b = -1
c = -2*x
d = (b**2) - (4*a*c)
sol1 = (-b-math.sqrt(d))/(2*a)
sol2 = (-b+math.sqrt(d))/(2*a)

if d>0:
    if sol1>0:
        print(sol1)
    else:
        print(sol2)

if d==0:
    print(sol1)





        

    


    