s=input()
bool=True
gar=''
for i in s:
    if i.isalpha():
        gar+=i
    else:
        z=gar
        for _ in range(int(i)):
            if bool:
                gar+=z[::-1]
                bool=not bool
            else:
                gar+=z
                bool=not bool
        bool=True
print(gar)