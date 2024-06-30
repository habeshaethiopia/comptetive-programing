from sys import stdin
from math import ceil

def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def solve():
    n=int(input())
    q=n//3
    r=n%3
    x=0
    
    if r:
        x=2 if r==1 and n%2 else 1
    a3=q+x
    print(a3)
    
    pass
if __name__=='__main__':
    for i in range(int(input())):
        solve()