# Problem: E - Consecutive Subarrays - https://codeforces.com/gym/523525/problem/E

from sys import stdin


def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def solve():
    n,k =invr()
    a=inlt()
    pre=[]
    x=0
    for i in a:
        x+=i
        pre.append(x)
    print(k*pre[-1]-(sum(sorted(pre[:-1])[:k-1])))
    pass
if __name__=='__main__':
    solve()