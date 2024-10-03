# Problem: Meaningless Operations - https://codeforces.com/problemset/problem/1110/C

from sys import stdin
from collections import Counter
from math import gcd

def largerstDevisor(x):
    ans=1
    i=2
    while i*i<x:
        if x%i==0:
            ans=max(i,ans)
            ans=max(ans, x//i)
        i+=1
    return ans
    
def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
def solve():
    a=int(input())
    byte=bin(a)[2:]
    inv="".join(['0'if i=='1' else '1' for i in byte])
    inv=int(inv,32)
    if inv==0:
        print(largerstDevisor(pow(2,len(byte))-1))
    else:
        print(pow(2,len(byte))-1)
    
if __name__=='__main__':
    for _ in range(int(input())):
        solve()