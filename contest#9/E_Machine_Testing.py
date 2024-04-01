from math import inf, ceil
for _ in range(int(input())):
    n=int(input())
    h=list(map(int, input().split()))
    p=list(map(int, input().split()))

    stack=[(inf,p[0])]
    ans=0
    for i in range(1,n):
        duration=0
        while h[i]-(stack[-1][0]-duration)*stack[-1][1]>0:
            t,pi=stack.pop()

            h[i]-=(t-duration)*pi
            duration+=t-duration
        duration+=ceil(h[i]/stack[-1][1])
        stack.append((duration, p[i]))
        ans=max(ans,duration)
    print(ans)
