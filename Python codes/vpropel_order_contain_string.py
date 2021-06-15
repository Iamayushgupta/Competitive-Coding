s1=input()
s2=input()
count=0
for i in range(len(s2)):
    if s2[i] not in s1:
        print("No")
        break
    else:
        x=s1[s1.index(s2[i])+1:]
        s1=x
        count+=1
if count==len(s2):
    print("Yes")
        