
    
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
    a=inlt()
    memo={}
    def dp(i,s,c):
        if (i,s,c) in memo:
            return memo[(i,s,c)]
        if i==len(a):
            return c
        if s+a[i]>=0:
            memo[(i,s,c)]=max(dp(i+1,s+a[i],c+1),dp(i+1,s,c) )
            return memo[(i,s,c)]
        else:
            memo[(i,s,c)]=dp(i+1,s,c)
            return memo[(i,s,c)]
    print(dp(0,0,0))

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()