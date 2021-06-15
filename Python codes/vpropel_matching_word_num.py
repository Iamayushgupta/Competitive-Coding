numstr=input()
w=input()
bool=True
temp=''
if len(numstr)!= 2*len(w):
    print('-1')
    bool= not bool
for i in range(len(w)):
    if ord(w[i])>90:
        x=str(ord(w[i])-70)
        temp+=x
    elif ord(w[i])>=65 and ord(w[i])<74:
        x='0' + str(ord(w[i])-64)
        temp+=x
    else:
        x=str(ord(w[i])-64)
        temp+=x
count=0
for i in range(0,len(numstr),2):
    if temp[i]==numstr[i] and temp[i+1]==numstr[i+1]:
        count+=1
if bool:
    print(count)