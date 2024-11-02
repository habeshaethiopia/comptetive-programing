from sys import stdin
from collections import Counter

def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
def solve():
    n=int(input())
    a=inlt()
    idx={a[i]: i+1 for i in range(n)}
    c=Counter(a)
    a.sort()
    a.sort(key=lambda x: c[x])
    # print(a)
    print(idx[a[0]] if c[a[0]]==1 else -1)
if __name__=='__main__':
    for i in range(int(input())):
        solve()