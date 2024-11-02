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
    k=int(input())
    print(100//gcd(k,100-k))
if __name__=='__main__':
    for _ in range(int(input())):
        solve()
