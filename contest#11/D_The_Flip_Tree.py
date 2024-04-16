from collections import defaultdict
n=int(input())
graph=defaultdict(list)
for i in range(n-1):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
init=list(map(int,input().split()))
goal=list(map(int,input().split()))

ans=[]
def flip():
    stack=[(1, 0,0)]
    visited=set()
    while stack:
        x, p, gp=stack.pop()
        visited.add(x)
        for i in graph[x]:
            if i not in visited:
                if gp%2==1:
                    if init[i-1]==goal[i-1]:
                        stack.append((i,gp+1,p))
                        ans.append(i)
                    else:
                        stack.append((i,gp,p))
                else:
                    if init[i-1]!=goal[i-1]:
                        stack.append((i,gp+1,p))
                        ans.append(i)
                    else:
                        stack.append((i,gp,p))       
flip()
ans=list(set(ans))
ans.sort()
print(len(ans))
print(*ans, sep='\n')