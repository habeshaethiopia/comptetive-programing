# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

from sys import stdin
from collections import defaultdict

def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def solve():
    n,m,k=invr()
    parent = {i:i for i in range(1, n+1) }
    size = [1] * (n+1)
    
    def find(x):
        if x != parent[x]:
             parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        parentX = find(x)
        parentY = find(y)
        if parentX != parentY:
             if size[parentX] > size[parentY]:
                 parent[parentY] = parentX
                 size[parentX] += size[parentY]
             else:
                 parent[parentX] = parentY
                 size[parentY] += size[parentX]    
    edges=[]
    for _ in range(m):
        u,v = invr()
        edges.append((u,v))
    query=[]
    cut=set()
    for _ in range(k):
        op, u, v = input().split()
        u=int(u)
        v=int(v)
        query.append((op, u, v) )
        if op =='cut':
            cut.add((u,v))
    for u,v in edges:
        if (u,v) not in cut and (v,u) not in cut:
            
            union(u,v)
    # print(parent, cut)
    ans=[]
    for op,u,v in query[::-1]:
        if op =='ask':
            ans.append('YES' if find(u)==find(v) else "NO")
            
        else:
            union(u,v)
        #     tree[u].remove(v)
        #     tree[v].remove(u)
    print(*ans[::-1], sep='\n')

if __name__=='__main__':
    solve()