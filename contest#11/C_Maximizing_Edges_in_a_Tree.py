from collections import defaultdict
n=int(input())
graph=defaultdict(list)
idx=[-1 for i in range(n+1)]
for i in range(n-1):
    s,e=map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(curr):
    stack=[curr]
    while stack:
        x=stack.pop()
        for i in graph[x]:
            if idx[i]==-1:
                if idx[x]==1:
                    idx[i]=0
                else:
                    idx[i]=1
                stack.append(i)
for i in graph:
    if idx[i]==-1:
        idx[i]==0
        dfs(i)
    
# print(idx)
# print(graph)
grop_A=set([i for i in range(n+1) if idx[i]==0])
grop_B=set([i for i in range(n+1) if idx[i]==1])
c=(len(grop_A)*len(grop_B))-n+1

print(c if c>0 else 0)




