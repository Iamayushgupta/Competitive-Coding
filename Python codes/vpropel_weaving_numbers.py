string1=input()
string2=input()
n=len(string1)
m=len(string2)
new1=''
new2=''
new3=''
new4=''

string3=string1[::-1]
string4=string2[::-1]

def new_string(a,b,c):
    for i in range(min(m,n)):
        c+=a[i]
        c+=b[i]
    if m>n:
        c+=b[n:]
    if n>m:
        c+=a[m:]
    return c
x=new_string(string1,string2,new1)
y=new_string(string2,string1,new2)
p=new_string(string3,string4,new3)
q=new_string(string4,string3,new4)

print(max(x,y,p,q))
