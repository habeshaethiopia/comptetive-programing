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
    small=min(a)
    for i in a:
        if i%small:
            print(-1)
            break
    else:
        print(small)
if __name__=='__main__':
    solve()
