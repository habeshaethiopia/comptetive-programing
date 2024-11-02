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
    s=[i for i in input()]
    k=int(input())
    cnt=Counter(s)
    if len(s)<k:
        print("impossible")
    else:
        x=k-len(cnt.keys())
        print( x if x>0 else 0)
    
if __name__=='__main__':
    solve()