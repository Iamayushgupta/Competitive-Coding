n=input()
count=0
bool = True

while True:
    asc = "".join(sorted(str(n)))
    dsc = "".join(sorted(str(n), reverse=True))
    if int(asc)-int(dsc)==0:
        break
    if len(str(int(dsc)-int(asc)))==2:
        z='0'+str(int(dsc)-int(asc))
    else:
        z=str(int(dsc)- int(asc))
    if z=='495':
        print(count)
        bool = not bool
        break
    n=z
    count+=1
if bool:
    print('No')
    
    
    

