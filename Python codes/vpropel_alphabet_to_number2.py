import string
x=int(input())
y=[]
for j in range(0,len(str(x))-1):
    p=(str(x)[j] + str(x)[j+1])
    k=int(p)
    while k>26:
        k=k-26
    y.append(k)
num2alpha = dict(zip(range(1, 27), string.ascii_lowercase))
z=[]
for num in y:
    q=num2alpha[num]
    z.append(q)
a=[]
for num in str(x):
    b=num2alpha[int(num)]
    a.append(b)

c=''.join([str(elem) for elem in a])
d=''.join([str(elem) for elem in z])
print(c)
print(d)