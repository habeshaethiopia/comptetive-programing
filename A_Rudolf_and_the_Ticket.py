from collections import Counter
for _ in range(int(input())):
    n, m, k= map(int, input().split())
    arrL=list(map(int, input().split()))
    arrR=list(map(int, input().split()))

    cntR=Counter(arrR)
    cntL=Counter(arrL)
    arrL.sort()
    arrR.sort()
    
    l=0
    r=0
    ans=0
    for i in arrL:
        for j in arrR:
            if i+j<=k:
                ans+=1
    print(ans)


    