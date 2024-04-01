from bisect import bisect_right
for _ in  range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    q=int(input())
    query=[]
    pri=[0]
    x=0
    for i in a:
        x+=i
        pri.append(x)
    # print(pri)
    for x in range(q):
        l,u= map(int, input().split())
        u=pri[l-1]+u
        ans=bisect_right(pri, u)
        flag=True
        if ans<len(pri) and abs(u-pri[ans])<=abs(u-pri[ans-1]):
            flag=False
        ans+=-1 if ans>l and flag else 0
        query.append(ans)
    print(*query)
    

