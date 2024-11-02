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
    n= int(input())
    a=inlt()
    x=0
    y=0
    b=[0]*n
    x=a[-1]
    b[-1]=x
    sign=1
    for i in range(n-2,-1,-1):
        b[i]=a[i]+x*sign
        sign*=-1
        x+=b[i]*sign
    print(*b)
    
if __name__=='__main__':
    solve()