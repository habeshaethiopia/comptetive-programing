x=list(map(int, input().split()))
n=x[0]-1
m=x[1]-1
matrix=[]

for i in range(n):
    row=list(map(int, input().split()))
    matrix.append(row)
turn=0
i=0
j=0
found=False
while i<n:
    while j<m:
        if (matrix[i][j]=='S' or matrix[i][j]=='T' )and not found:
            found=True
        else:
            j+=1
        if found:
            if matrix[i][j]=='*':
                i+=1
                turn+=1
            elif matrix[i][j]=='.':
                j+=1

        

