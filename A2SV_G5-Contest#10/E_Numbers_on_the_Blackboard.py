from math import gcd
for _ in range(int(input())):
    n, k = map(int, input().split())
    a= list(map(int, input().split()))
    if len(set(a))==1:
        print(0)
    elif min(a)>k or max(a)<k:

        gc=0
        for i in a:
            gc=gcd(gc,abs(i-k))
        ans=0
        for i in a:
            ans+=(abs(i-k)//gc)-1
        print(ans)
    else:
        print(-1)
