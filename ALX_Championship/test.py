import sys
from collections import Counter
from heapq import heappop, heappush
sys.stdin = open('kfib.in', 'r')
sys.stdout = open('kfib.out', 'w')
# input_data = sys.stdin.readlines()
def input(): return sys.stdin.readline().strip()
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
    print(g , sep='\n')
    print('hi')
solve()