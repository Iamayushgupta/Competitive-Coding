# MARCH-8TH IN PYTHON
l=list(input().split())
l1=''.join(l)
print(l1)
v=['A','E','I','O','U']
def check_vowels(x):
    count=0
    for i in x:
        if i in v:
            count+=1
    return count
    
def check_word(ele):
    count=0
    temp=l.copy()
    temp.remove(ele)
    print(temp)
    for i in ele:
        for x in temp:
            if i in x:
                if check_vowels(ele)==check_vowels(x):
                    count+=1
    if count==len(ele):
        return True

for ele in l:
    check_word(ele)


        
                    
        