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
    n,m=invr()
    res=n//m
    rem=n%m
    for i in range(m):
        if rem:
            print(res+1, end=" ")
            rem-=1
        else:
            print(res, end=" ")
    print()

if __name__=='__main__':
    solve()
    