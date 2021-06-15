line1=input().split()

strength=int(line1[0])
number_dragons=int(line1[1])

list1=[]
for i in range(0,number_dragons):
    line_n=input().split()
    list1.append((int(line_n[0]),int(line_n[1])))

list1.sort()

bool=True

for i in range(number_dragons):
    if list1[i][0]>strength:
        print("NO")
        break
    else:
        strength+=list1[i][1]
        bool=not bool

if bool:
    print("YES")

    