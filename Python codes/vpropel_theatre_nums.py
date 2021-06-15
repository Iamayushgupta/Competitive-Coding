word=input()
n=int(input())
bool=True
dic1={}
dic2={}
x=n%len(word)
for i in range(n):
    dic1[i+1]=word[i%len(word)]
for i in range(n,0,-1):
    dic2[i]=word[x%len(word)]
    x=x+1

for i in range(n,0,-1):
    if dic1.get(i)==dic2.get(i):
        print(i)
        bool=not bool
        break
        
if bool:
    print('-1')
    
        
