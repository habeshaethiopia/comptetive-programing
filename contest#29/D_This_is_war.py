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
    m=0
    ans=1
    for i in range(n):
        if a[i]>m:
            m=a[i]
            ans=i+1
    print(ans)
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
