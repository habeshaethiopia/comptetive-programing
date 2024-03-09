from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    arr=[int(i) for i in input()]
    x=0
    pri=defaultdict(int)
    pri[0]=1
    ans=0
    for i in arr:
        x+=i
        pri[i]=x
        if x-i in pri:
            ans+=pri[x-i]
    print(pri)
    print( ans)
    


