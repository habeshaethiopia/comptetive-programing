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
    n,m =invr()
    s=input()
    cnt=Counter(s)
    # print(cnt.values())
    if len(cnt)<m:
        print(0)
    else:
        print(min(cnt.values())*m)
if __name__=='__main__':
    solve()