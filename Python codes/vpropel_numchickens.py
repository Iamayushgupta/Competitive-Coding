n=int(input('enter number of chickens: '))
m=int(input('enter minimum chickens: '))

bool = True

for i in range(m,n,2):
    for j in range(i+2,n,2):
            k = n-(i+j)
            if (k <= j):
                break

            print(i,j,k)
            bool = False
if bool:
    print("No way")