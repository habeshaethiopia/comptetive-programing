from collections import Counter
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    num=Counter(a)
    l=0
    r=0
    c=[]

    while r<len(num):
        c.append([a[l],a[r],r-l+1])

        if num[a[r]]>=k:
            r+=num[a[r]]
        else:
            r+=1
            l+=r
    print(c)    
         
