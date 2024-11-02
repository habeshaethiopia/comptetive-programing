from sys import stdin
from collections import Counter
import sys
sys.stdin = open('kfib.in', 'r')
sys.stdout = open('kfib.out', 'w')
input_data = sys.stdin.readlines()
def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
def solve():
    pass
if __name__=='__main__':
    solve()