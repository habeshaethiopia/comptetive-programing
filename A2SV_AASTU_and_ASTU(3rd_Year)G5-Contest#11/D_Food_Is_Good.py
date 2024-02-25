for _ in range(int(input())):
    n=int(input())
    nums=list(map(int,input().split()))
    ans=[]
    x=0
    for i in nums:
        x+=i
        ans.append(x)
    print(ans)
    if ans[-1]<max(ans):
        print('NO')
    else:
        print('YES')