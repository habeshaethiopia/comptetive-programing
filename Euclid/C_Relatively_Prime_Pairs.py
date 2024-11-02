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
    l,r = invr()
    
    i=0
    print("YES")
    while i<r-l+1:
        print(l+i,l+i+1)
        i+=2

if __name__=='__main__':
    solve()


