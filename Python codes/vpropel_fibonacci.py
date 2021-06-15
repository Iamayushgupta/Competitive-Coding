n=int(input())
n1=0
n2=1
x=['0']
nth=0
while n2<=n:
  nth=n2+n1
  x.append(nth)
  n1=n2
  n2=nth
y=[]
for i in x:
  if str(i) in str(n):
    y.append(i)

if len(y)==0:
  print('none')
else:
  for j in y:
    print(j)
    


