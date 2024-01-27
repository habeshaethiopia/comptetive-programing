import math
for _ in range(int(input())):
        n = int(input())
        E = list(map(int, input().split()))
        s=math.floor(sum(E)/2)
        E.sort(reverse=True)
        ans=math.ceil(sum(E)/2)
        for i in range(n):
                if s>0:
                    if s-E[i] >=0:
                        s-=E[i]
                        ans+=1
                        
                    else:
                        ans+=1
                        break
        print(ans)