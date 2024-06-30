
import sys, threading
from sys import stdin


def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def main():
    n,k=invr()
    h=inlt()
    memo={}
    dp=[0]*(n)
    for i in range(1,n):
        mn=float('inf')
        for step in range(1,k+1):
            # print(step)
            if i-step >=0:
                mn=min(mn, dp[i-step]+abs(h[i]-h[i-step]))
            else:
                break
        dp[i]=mn

    print(dp[-1])
    
if __name__ == '__main__':
    main()