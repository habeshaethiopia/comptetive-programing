from sys import stdin
from collections import Counter
from math import gcd

def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
def solve():
    a,b = invr()
    if abs(a-b) >=1:
        print(1)
    else:
        print(a)
if __name__=='__main__':
    solve()