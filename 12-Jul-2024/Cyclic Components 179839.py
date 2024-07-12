# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

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
visited = set()
def dfs(graph, start_node):
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
def solve():
    n,e=invr()
    graph=defaultdict(list)
    for i in range(e):
        u,v=invr()
        u-=1
        v-=1
        graph[u].append(v)
        graph[v].append(u)
    # print(graph)
    for i in range(n):
        if len(graph[i])!=2 and i not in visited:
            dfs(graph,i)
    ans=0
    for i in range(n):
        if i not in visited:
            ans+=1
            dfs(graph,i)
    print(ans)
    

    
    pass
if __name__=='__main__':
    solve()