
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
    n=int(input())
    h=inlt()
    memo={}
    def dp(i):
        if i in memo:
            return memo[i]
        if i==n-1:
            return 0
        if i>=n:
            return float('inf')
        t1=dp(i+1)+abs(h[i+1]-h[i] if i+1<n else float('inf'))
        t2=dp(i+2)+abs(h[i+2]-h[i] if i+2<n else float('inf'))
        # print(min(t1,t2),i)
        memo[i]=min(t1,t2)
        return min(t1,t2)
    print(dp(0))

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()