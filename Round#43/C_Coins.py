from sys import stdin
from collections import Counter
import sys, threading
def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
def main():
    memo={1:1,2:2, 0:0}
    for i in range(int(input())):
        n= int(input())
        def dp(n):
            if n in memo:
                return memo[n]
            y,z=float("inf"), float("inf")
            if n>=3:
                y=dp(n-3)
            if n>=5:
                z=dp(n-5)
            x=min(y,z)
            memo[n]=x
            return memo[n]
        ans=dp(n)
        
        print(ans)
        



# if __name__=='__main__':
#     for i in range(int(input())):
#         solve()

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()