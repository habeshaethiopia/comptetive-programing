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
    a,b,n=invr()
    start=a
    turn=0
    player=[a,b]
    while n - gcd(n,start)>=0:
        n-=gcd(n,start)
        turn^=1
        start=player[turn]
    print(turn^1)

if __name__=='__main__':
    solve()