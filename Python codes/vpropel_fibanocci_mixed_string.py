import string
s1=input()
s2=input()
n=int(input())

num2alpha = dict(zip(range(1, 27), string.ascii_lowercase))

def letter_add(list_num):
  str1=''
  for ele in list_num:
    c=ord(ele)-95
    if c==27:
      str1+='a'
    else:
      z=num2alpha[c]
      str1+=z
  return str1

num=0
while num<n-2:
    list1=list(s1.strip())
    list2=list(s2.strip())

    x=letter_add(list1)
    y=letter_add(list2)
    
            
    final=''
    for i in range(0,len(s1)):
        if i%2==0:
            final+=x[i]
        else:
            final+=y[i]

    num+=1
    s1=s2
    s2=final

print(final)