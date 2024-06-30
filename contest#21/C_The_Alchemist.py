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
def dfs(graph, start_node,c):
    visited = set()
    stack = [start_node]
    mincost=0
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    
def solve():
    n,k=invr()
    c=inlt()
    p=set(inlt())
    for i in range(c):
        if i+1 in p:
            c[i]=0
    ans=[0]*n
    # print(p)
    tree=defaultdict(list)
    for i in range(n):
        L4=inlt()
        m=L4[0]
        tree[i].extend(L4[1:])
    
    print(tree)       
if __name__=='__main__':
    for _ in range(int(input())):
        solve()