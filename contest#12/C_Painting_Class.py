from sys import stdin


def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
from collections import defaultdict 
from collections import deque



def bfs(graph, start_node,clour,c):
    visited = set()
    queue = deque([(start_node,clour)])
    ans=0
    while queue:
        for i in range(len(queue)):
            node,nc = queue.popleft()
            visited.add(node)
            if nc!=c[node-1]:
                ans+=1
                nc=c[node-1]    
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor,nc))
    return ans

def solve():
    
    n=int(input())
    p=inlt()
    c=inlt()
    graph=defaultdict(list)
    for i in range(n-1):
        u,v=i+2, p[i]
        graph[u].append(v)
        graph[v].append(u)
    # print(graph)
    
    print(bfs(graph,1,0,c))









if __name__=='__main__':
    solve()
