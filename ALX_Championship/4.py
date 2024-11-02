import sys
from collections import Counter,defaultdict
from heapq import heappop, heappush
sys.stdin = open('prescription.in', 'r')
sys.stdout = open('prescription.out', 'w')
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
    n,m = invr()
    pre=[]
    for i in range(m):
        med=inlt()
        pre.append(med)
    a=inlt()
    pre.sort(reverse=True)
    print(pre)
    

if __name__=="__main__": 
    solve()