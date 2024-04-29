n,m=map(int, input().split())


root = [i for i in range(n)]
size = [1] * n
def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(self, x, y):
    rootX =  find(x)
    rootY =  find(y)
    if rootX != rootY:
        if  size[rootX] >  size[rootY]:
            root[rootY] = rootX
            size[rootX] +=  size[rootY]
        else:
            root[rootX] = rootY
            size[rootY] +=  size[rootX]
for _ in range(m):
    com=input().split()
    if len(com)==3:
        union(int(com[1])-1, int(com[2])-1)
    else:
        
#topological sort

from collections import deque
from typing import Dict, List

def topoSort(V: int, adj:Dict) -> List[int]:
    q: deque = deque()
    indegree: List[int] = [0] * V

    # finding indegree of nodes
    for i in range(V):
        for it in adj.get(i, []):
            indegree[it] += 1

    # add nodes having 0 indegree
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)

    i: int = 0
    topo: List[int] = [0] * V

    # BFS
    while q:
        node: int = q.popleft()
        topo[i] = node
        i += 1

        for it in adj.get(node, []):
            indegree[it] -= 1
            if indegree[it] == 0:
                q.append(it)

    return topo
