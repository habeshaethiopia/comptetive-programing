
sm=0
n=int(input())
leftdiagonal={}
rightdiagonal={}
matrix=[]
for i in range(n):
    row=list(map(int, input().split()))
    matrix.append(row)
for i in range(n):
    for j in range(n):
        if i-j==0:
            sm+=matrix[i][j]
        if i+j == n-1:
            sm+=matrix[i][j]
        if i==(n-1)//2:
            sm+=matrix[i][j]
        if j==(n-1)//2:
            sm+=matrix[i][j]
print(sm-3*matrix[(n-1)//2][(n-1)//2])   