x=input()
z=[]
for i in range(0,len(x)):
    y=x[len(x)-1] + x[:len(x)-1]
    if y not in z:
        z.append(y)
        x=y
print(len(z))
