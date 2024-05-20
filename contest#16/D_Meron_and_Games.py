
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
    buk=[0 for i in range(max(a)+1)]

    for i in range(n):
        buk[a[i]]+=a[i]
    m=len(buk)
    memo={}
    def coin(i):
        if i>=m:
            return 0
        if i in memo:
            return memo[i]
        take=coin(i+2)+buk[i]
        leave=coin(i+1)
        memo[i]=max(take,leave)
        return max(take,leave)
    print(coin(0))
        

        
    pass

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()