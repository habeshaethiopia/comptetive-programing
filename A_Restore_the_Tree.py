from sys import stdin
from collections import defaultdict,deque

def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def solve():
    n,m=invr()
    graph=defaultdict(list)
    indegree=[0 for i in range(n)]
    for i in range(n-1+m):
        a,b=invr()
        graph[a].append(b)
        indegree[b-1]+=1

    q=deque()
    pri=None
    ans=[-1  for i in range(n)]
    for i in range(n):
        if not indegree[i]:
            q.append(i+1)
            ans[i]=0
           
    
    while q:
        parent=q.popleft()
        for ch in graph[parent]:
            indegree[ch-1]-=1
            if indegree[ch-1]==0:
                ans[ch-1]=parent
                q.append(ch)
    print(*ans, sep='\n')






 


    
if __name__=='__main__':
    solve()