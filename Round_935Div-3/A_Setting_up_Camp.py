from math import ceil
for _ in range(int(input())):
    i,e,u=map(int, input().split())
    ans=i
    flag=True
    if e%3==0:
        ans+=e//3+ceil(u/3)
    else:
        if u>=3-e%3:
            u-=3-e%3
            e+=3-e%3
            res=e//3
            ans+=res
            ans+=ceil(u/3)
        else:
            flag=False
            print(-1)
    if flag:
        print(ans)