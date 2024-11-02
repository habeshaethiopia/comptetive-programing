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
    n, l, r, k=invr()
    a=inlt()
    c=0
    a.sort()
    for i in a:
        if i>=l and i<=r and i<=k:
            c+=1
            k-=i

    print( c)

if __name__=='__main__':
    for  _ in range(int(input())):
        solve()