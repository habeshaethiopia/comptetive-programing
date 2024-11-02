from sys import stdin
from collections import Counter,defaultdict

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
    employee=defaultdict(list)
    for i in range(n-1):
        employee[a[i]].append(i+2)
    print(employee)
    

if __name__=='__main__':
    for _ in range(int(input())):
        solve()