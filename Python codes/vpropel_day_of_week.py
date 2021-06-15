n=int(input())
dic={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
a=int(input())
m=int(input())
if m>n:
    print(dic[(a+(m-n)%7)%7])
else:
    print(dic[(a-(n-m)%7)%7])