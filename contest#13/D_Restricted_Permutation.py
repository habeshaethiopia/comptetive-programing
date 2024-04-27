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
    
    n,m=invr()
    ans=0
    graph=defaultdict(list)
    for i in range(m):
        a,b=invr()
        graph[a].append(b)
    print(graph)
    
if __name__=='__main__':
    solve()