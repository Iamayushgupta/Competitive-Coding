n=int(input())
x=''
for i in range(len(str(n))):
    y=9-int(str(n)[i])
    
    if y>int(str(n)[i]):
        x+=str(n)[i]

    else:
        x+=str(y)

if int(x[0])==0:
    print('9' + x[1:])
else:
    print(x)
