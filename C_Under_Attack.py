for i in range(int(input())):
    x=list(map(int, input().split()))
    n=x[0]
    m=x[1]
    matrix=[]
    sm=[]
    mx=0
    leftdiagonal={}
    rightdiagonal={}

    for i in range(n):
        row=list(map(int, input().split()))
        matrix.append(row)
    for i in range(n):
        for j in range(m):
            temp=0
            
            t1=i
            t2=j
            while j<m and  i<n:
                temp+=matrix[i][j]
                i+=1
                j+=1
            i=t1
            j=t2


            while i>=0 and j>=0 :
                temp+=matrix[i][j]
                i-=1
                j-=1
            i=t1
            j=t2
            temp-=matrix[i][j]
            
            
            while i>=0 and j<m :
                temp+=matrix[i][j]
                i-=1
                j+=1
            i=t1
            j=t2
            temp-=matrix[i][j]
            
            
            while i<n  and j>=0:
                temp+=matrix[i][j]
                i+=1
                j-=1
            i=t1
            j=t2
            temp-=matrix[i][j]
            mx=max(mx,temp)
    print(mx)
    