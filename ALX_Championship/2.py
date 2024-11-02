import sys
from collections import Counter
from heapq import heappop, heappush
sys.stdin = open('committee.in', 'r')
sys.stdout = open('committee.out', 'w')
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
    mtx=[]
    ans={}
    
    for i in range(n):
        x=sum(inlt())
        if x not in ans:
            ans[x]=i+1
        mtx.append(x)
    print(ans[min(mtx)], ans[max(mtx)])
    
    
solve()