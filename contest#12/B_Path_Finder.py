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

from collections import deque


def bfs(graph, start_node,c):
    visited = set()
    queue = deque([(start_node,c)])
    ans=0
    while queue:
        for i in range(len(queue)):
            node,w = queue.popleft()
            visited.add(node)

            for neighbor,l in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor,l+w))
                    ans=max(ans,l+w)
    return ans
def solve():
    
    n=int(input())
    graph=defaultdict(list)
    for i in range(n-1):
        u,v,c=inlt()
        graph[u].append((v,c))
        graph[v].append((u,c))
    ans=bfs(graph,0,0)
    # print(graph)
    print(ans)
if __name__=='__main__':
    solve()