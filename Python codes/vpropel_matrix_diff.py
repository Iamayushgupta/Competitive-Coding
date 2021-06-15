r1=int(input())
c1=int(input())
matrix1=[]
for i in range(0,r1):
    row_ele=list(map(int,input().split())) 
    matrix1.append(row_ele)

r2=int(input())
c2=int(input())
ele_of_matrix2=[]
for i in range(0,r2):
    row_ele=list(map(int,input().split()))
    ele_of_matrix2 += row_ele

for i in range(0,r1):
    for j in range(0,c1):
        if matrix1[i][j] in ele_of_matrix2:
            matrix1[i][j]=0

for i in range(0,r1):
    for j in range(0,c1):
        print(matrix1[i][j],end=' ')
    print()
