from collections import defaultdict
for i in range(int(input())):
    x=list(map(int, input().split()))
    n=x[0]
    m=x[1]
    matrix=[]
    sm=[]
    mx=0
    leftdiagonal=defaultdict(int)
    rightdiagonal=defaultdict(int)

    for i in range(n):
        row=list(map(int, input().split()))
        matrix.append(row)
    for i in range(n):
        for j in range(m):
            leftdiagonal[i+j]+=matrix[i][j]
            rightdiagonal[i-j]+=matrix[i][j]
    for i in range(n):
        for j in range(m):
            temp=leftdiagonal[i+j]+rightdiagonal[i-j]-matrix[i][j]
            mx=max(mx,temp)
    print(mx)
    