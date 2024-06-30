
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
    a=[]
    b=[]
    c=[]
    n=int(input())
    for i in range(n):
        ai,bi,ci=invr()
        a.append(ai)
        b.append(bi)
        c.append(ci)
    memo={}
    def dp(i,x):
        
        if (i,x) in memo:
            return memo[(i,x)]
        if i>=n:
            # print(n)
            return 0
        xa=0
        xb=0
        xc=0
        if x!='a':
            xa=a[i]+dp(i+1,'a')
        if x!='b':
            xb=b[i]+dp(i+1,'b')
        if x!='c':
            xc=c[i]+dp(i+1,'c')
        memo[(i,x)]=max(xa,xb,xc)    
        return max(xa,xb,xc)    
    print(dp(0,''))


    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
