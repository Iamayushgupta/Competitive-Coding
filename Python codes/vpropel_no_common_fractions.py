x=int(input())
y=int(input())
count=0
l=[]
for i in range(y,x+1):
    for j in range(i+1,x+1):
        z=i/j
        if z>0.2 and z<0.6:
            if z not in l:
                l.append(z)
            
        
print(len(l))