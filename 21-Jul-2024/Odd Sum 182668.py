# Problem: Odd Sum - https://codeforces.com/problemset/problem/797/B

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
    n=int(input())
    a=inlt()
    ans=-float('inf')
    x=0
    po=float('inf')
    no=-float('inf')
    # print(a)
    for i in a:
        if i>0:
            x+=i
            if i%2:
                po=min(po,i)
        else:
            if i%2:
                no=max(no,i)
    if x%2==0:
        x-=min(po,-no)
    print(x)
        
    # print(ans)
    pass
if __name__=='__main__':
    solve()