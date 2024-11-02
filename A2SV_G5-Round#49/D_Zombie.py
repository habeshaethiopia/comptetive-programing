from sys import stdin
from collections import Counter, defaultdict,deque

def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))


def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    ans=0
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        ans+=1
    # print(ans, start_node)
    return ans-1
def solve():
    n,m=invr()
    g=defaultdict(list)
    for i in range(m):
        u,v=invr()
        g[u].append(v)
        g[v].append(u)
    ans=0
    for i in g:
        ans=max(ans,bfs(g,i))
    print(ans)
if __name__=='__main__':
    solve()