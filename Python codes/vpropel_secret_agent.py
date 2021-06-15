w1=input()
w2=input()
z=min(len(w1),len(w2))
i=-1
carry=0
num=''
while abs(i)!=z+1:
    x=ord(w1[i]) + ord(w2[i]) + carry
    num+=str(x)[-1]
    carry=int(str(x)[:2])
    i=i-1
if len(w1)<len(w2):
    while abs(i)!=len(w2)+1:
        t=ord(w2[i]) + carry
        num+=str(t)[-1]
        carry=int(str(t)[:2])
        if abs(i)==len(w2):
            num+=str(carry)[::-1]
        i=i-1

elif len(w2)<len(w1):
    while abs(i)!=len(w1)+1:
        t=ord(w1[i]) + carry
        num+=str(t)[-1]
        carry=int(str(t)[:2])
        if abs(i)==len(w1):
            num+=str(carry)[::-1]
        i=i-1
else:
    num+=str(carry)[::-1]

num=num[::-1]

def code(x):
    temp=''
    temp+=chr(((int(num[:2])+1)%26)+96)
    for i in range(2,len(x)):
        temp+=chr(((int(num[i])+1)%26)+96)
    return temp
print(code(num))
