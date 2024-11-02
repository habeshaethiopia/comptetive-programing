import sys
from collections import Counter,defaultdict
from math import ceil
from heapq import heappop, heappush
sys.stdin = open('connected.in', 'r')
sys.stdout = open('connected.out', 'w')
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
    ex=0
    graph=defaultdict(list)
    for i in range(m):
        u,v =invr()
        graph[u].append(v)
        graph[v].append(u)
    print(ceil((n-m-1)/len(graph)))
    print(n-1-m)
    

if __name__=="__main__": 
    solve()