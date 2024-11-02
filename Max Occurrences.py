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
    if n>2:
        print(4)
    else:
        print(n)
if __name__=='__main__':
    for _ in range(int(input())):
        solve()