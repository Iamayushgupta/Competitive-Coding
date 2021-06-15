n=int(input())
m=int(input())
l=[]
bool= True
for i in range(n):
    l.append(input().split())
code=input()

def check(ele):
    count=0
    for i in code:
        if i in ele:
            count+=1
    if count==len(code):
        return True
def l_to_str(temp):
    temp.sort()
    s=''
    for i in temp:
        s+=i
    return s

l2=[]
for i in range(m):
    s1=''
    for j in range(n):
        s1+=l[j][i]
        l2.append(s1)
def check_col(var):
    count=0
    for i in code:
        if i in var:
            count+=1
    if count==len(code):
        return True
flag=0       
for i in l:
    if check(i):
        print(l_to_str(i))
        print('Lucky Player')

    if i==l[-1]:    
        for ele in l2:
            if check_col(ele):
                ele = ''.join(sorted(ele))
                print(ele)
                print('Lucky Player')
                exit()
            if ele==l2[-1]:
                print('Unlucky Player')
                exit()




    