from math import ceil ,floor
for i in range(int(input())):
    n=int(input())
    matrix=[]
    c=0
    for i in range(n):
        row=[i for i in input()]
        matrix.append(row)
   
    for i in range(floor(n/2)):
        for j in range(ceil(n/2)):
            corr=[matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j],matrix[n-1-j][i]]
            # print(corr)
            n0=corr.count('0')
            c+=min(4-n0,n0)
            
    print(c)
