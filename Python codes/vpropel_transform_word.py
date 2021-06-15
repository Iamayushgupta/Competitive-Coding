word=input()
list1=[]
for i in range(len(word)):
    x=int(input())
    list1.append(x)
    
temp=''
for i in range(0,len(word)):
    temp+=word[list1.index(i+1)]
print(temp)
for i in range(len(word)):
    print(word.index(temp[i])+1)
    


