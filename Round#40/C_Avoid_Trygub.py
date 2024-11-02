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
    s=[i for i in input()]
    ans=""
    cnt=0
    for i in s:
        if i=='t':
            cnt+=1
        else:
            ans+=i
    print(ans+"t"*cnt)
if __name__=='__main__':
    for _ in range(int(input())):
        solve()