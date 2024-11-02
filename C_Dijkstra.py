from sys import stdin
from collections import Counter
from heapq import heappop, heappush
import sys
sys.stdin = open('kfib.in', 'r')
sys.stdout = open('kfib.out', 'w')
input_data = sys.stdin.readlines()

def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
def solve():
    n,m = invr()
    dist=[float('inf')]*n
    dist[0]=0
    p=[-1]*n
    q=[(0,0)]
    g=[[]for i in range(n)]
    for i in range(m):
        u,v,w=invr()
        u-=1
        v-=1
        g[u]+=[(v,w)]
        g[v]+=[(u,w)]
    # print(g)
    while q:
        a=heappop(q)[1]
        for v,w in g[a]:
            if dist[v]>dist[a]+w:
                dist[v]=dist[a]+w
                p[v]=a
                heappush(q,(dist[v], v))
    if dist[n-1]==float('inf'):
        print(-1)
    else:
        i,ans=n-1, []
        while i!=-1:
            ans+=[i+1]
            i=p[i]
        print(*ans[::-1])

if __name__=='__main__':
    solve()