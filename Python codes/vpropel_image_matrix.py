n= int(input())  
matrix = [] 
for i in range(n):		 
	a =[] 
	for j in range(n):	 
		a.append(int(input())) 
	matrix.append(a) 

matrix1 =[]
for i in range(len(matrix)):
    temp = []
    for j in range(len(matrix[i])):
        temp.append(matrix[i][j])
    matrix1.append(temp)

if n==2:
    matrix1[0][0]=matrix[1][1]
    matrix1[1][1]=matrix[0][0]
    matrix1[0][1]=matrix[1][0]
    matrix1[1][0]=matrix[0][1]


if n%2==0:
    for i in range(0,n-2,2):
        matrix1[0][i]=matrix[0][i+2]
        matrix1[0][n-2]=matrix[1][n-1]
        matrix1[i+2][0]=matrix[i][0]

    for i in range(1,n-2,2):
        matrix1[i][n-1]=matrix[i+2][n-1]
        matrix1[n-1][1]=matrix[n-2][0]
        matrix1[n-1][i+2]=matrix[n-1][i]

else:
    for i in range(0,n-2,2):
        matrix1[0][i]=matrix[0][i+2]
        matrix1[i][n-1]=matrix[i+2][n-1]
        matrix1[i+2][0]=matrix[i][0]
        matrix1[n-1][i+2]=matrix[n-1][i]

        
for i in range(n): 
	for j in range(n): 
		print(matrix1[i][j], end = "\t") 
	print()
