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
    n, a, b= invr()
    h= inlt()
    h.sort(reverse=True)
    x=h[a-1]-h[a]
    print(x)
        

if __name__=='__main__':
    solve()