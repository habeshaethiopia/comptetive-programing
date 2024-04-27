from sys import stdin
from heapq import heappush,heappop

def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def solve():
    
    for _ in range(int(input())):
        n=int(input())
        s=inlt()
        stack=[]
        ans=0
        for i in s:
            if i!=0:
                heappush(stack,-i)
            else:
                if stack:
                    ans+=-heappop(stack)
        print(ans)  

if __name__=='__main__':
    solve()