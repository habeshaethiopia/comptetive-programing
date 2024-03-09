for _ in range(int(input())):
    input()
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans=[]
    for i in range(1,n+1):
        temp=   float('inf')
        for j in range(k):
            temp=min(temp,t[j]+abs(a[j]-i))
        ans.append(temp)
    print(*ans)

