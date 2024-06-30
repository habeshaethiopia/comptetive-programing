# Problem: A - Ascend - https://codeforces.com/gym/526229/problem/A

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
    dp=[0]*(n+1)
    ans=0
    c=1
    for i in range(1,n):
        if a[i-1]<a[i]:
            c+=1
        else:
            ans=max(c,ans)
            c=1
    ans=max(ans,c)
    print(ans)
    

    
    pass
if __name__=='__main__':
    solve()