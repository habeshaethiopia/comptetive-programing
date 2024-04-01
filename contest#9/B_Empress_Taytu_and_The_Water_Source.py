from math import ceil
for _ in range(int (input())):
    n,k=map(int, input().split())
    d=list(map(int, input().split()))
    a=list(map(int, input().split()))
   
    
    def help(s):
        x=0
        for i in range(len(d)):
            x+=ceil(d[i]/s)*a[i]
        # print('x:',x)
        return x
    if sum(a)>k:
        print(-1)
    else:
        l=1
        r=max(d)
        while l<=r:
            mid=(l+r)//2
            # print(mid)
            if help(mid)>k:
                l=mid+1
            else:
                r=mid-1
        print(l)