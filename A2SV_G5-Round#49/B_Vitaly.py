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
    a.sort()
    idx=a.index(0)
    nv=idx
    pv=n-idx-1
    print(1,a[0])
    if pv:
        print(pv, *[a[i] for i in range(idx+1,n)])
        print(idx, *[a[i] for i in range(1,idx+1)])
    else:
        r=nv-1 if (nv-1)%2==0 else nv-2
        print(r, *[a[i] for  i in range(1,r+1)])
        print(idx-r, *[a[i] for i in range(r+1,idx+1)])

    print()
if __name__=='__main__':
    solve()