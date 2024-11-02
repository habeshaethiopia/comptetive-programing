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
    l, r, d=invr()
    m=1
    if d<l:
        print(d)
    else:
        m=r//d+1
        print(d*m)
if __name__=='__main__':
    for  i in range(int(input())):
        solve()