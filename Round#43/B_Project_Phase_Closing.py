from sys import stdin
from collections import Counter
from math import ceil

def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
def solve():
    n,m,k=invr()
    idx=ceil(k/2)
    x=ceil(idx/m)
    # print(idx,"xxx")
    print(x, idx%(m) if  idx%(m) else m, "L" if k%2 else "R" )
if __name__=='__main__':
    solve()