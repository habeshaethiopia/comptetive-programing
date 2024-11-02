import sys
from collections import Counter
from heapq import heappop, heappush
sys.stdin = open('dsum.in', 'r')
sys.stdout = open('dsum.out', 'w')
# input_data = sys.stdin.readlines()
def input(): return sys.stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
def solve():
    a=[int(i) for i in input()]
    print(sum(a))
solve()