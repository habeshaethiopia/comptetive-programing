from sys import stdin
from collections import Counter
from math import floor

def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
def solve():
    n,k =invr()
    p=inlt()
    ans=0
    m=1
    for i in range(n):
        x=1
        while x!=m:
            x*=0.5
            p[i]=floor(p[i]*0.5)
        temp=p[i]-k
        if temp>=0 and temp >= floor(p[i]*0.5):
            ans+=temp
        else:
            m*= 0.5
            
            ans+=floor(p[i]*0.5)
    print(ans)



if __name__=='__main__':
    for _ in range(int(input())):
        solve()