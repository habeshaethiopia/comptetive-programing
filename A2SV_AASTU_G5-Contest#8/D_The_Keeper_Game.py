for _ in range(int(input())):
    n=int(input())
    s=input()
    x=0
    cost=0
    left=[]
    for i in s:
        if i=='*':
            x+=1
        else:
            cost+=x
        left.append(cost)
    x=0
    cost=0
    right=[]
    for i in s[::-1]:
        if i=='*':
            x+=1
        else:
            cost+=x
        right.append(cost)
    right=right[::-1]
    ans=float('inf')
    for i in range(len(left)):
        ans=min(ans,left[i]+right[i])
    print(ans)

    

