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
    n=input()
    s=input()

    if s[0]==s[-1]:
        print("No")
    else:
        print("YES")
if __name__=='__main__':
    for _ in range(int(input())):
        solve()