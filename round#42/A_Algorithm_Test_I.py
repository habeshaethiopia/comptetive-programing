from sys import stdin
from collections import Counter
from math import factorial

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
    a=set(inlt())
    print(factorial(len(a)))
if __name__=='__main__':
    solve()