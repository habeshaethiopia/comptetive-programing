n = int(input())

s=list(map(int,input().split()))
res=sum(s)
if res%2==0:
    print(res)
else:
    s.sort()
    s.sort(key= lambda i:i%2,reverse=True )
    res -= s[0]
    if res%2==0:
        print(res)
    

