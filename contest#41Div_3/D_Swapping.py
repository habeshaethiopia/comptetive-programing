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
    n,x,m =invr()
    ml,mr=float("inf"), 0
    for i in range(m):
        l,r=invr()
        ml=min(ml,l)
        mr=max(mr,r)

    print(mr-ml+1)
if __name__=='__main__':
    for  i in range(int(input())):
        solve()