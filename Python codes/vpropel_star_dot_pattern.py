n=int(input())
x=-1
for i in range(n,0,-1):
    if i==n:
        print('. '*(i-1) + '*' + ' .'*(i-1))
    else:
        print('. '*(i-1) + '* '+ '. '*x + '*'+ ' .'*(i-1))
    x+=2
        