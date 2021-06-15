l1=input()
h=int(input())%12
m=int(input())
new=ord(l1)
dic={}
dic[0]=new+22

for i in range(1,13):
    dic[i]=new
    new+=2

if m>0:
    print('Between ' + str(chr(dic[h])) + ' and ' +  str(chr(dic[h+1])))
else:
    print("On " + str(chr(dic[h])))
if m==0:
    print('On ' + str(chr(dic[12])))
else:
    if m%5==0:
        print("On " + str(chr(dic[m/5])))
    else:
        print("Between " + str(chr(dic[m//5])) + ' and ' + str(chr(dic[(m//5) + 1])))
