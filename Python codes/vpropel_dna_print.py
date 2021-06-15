from itertools import combinations 
dna=input()
length=int(input())
x=[]
for i in combinations(dna,length):
    y=''.join(i)
    x.append(y)
x.sort()
print(x)