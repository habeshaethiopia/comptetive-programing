import sys
from collections import Counter,defaultdict
from heapq import heappop, heappush
from math import sqrt
sys.stdin = open('expression.in', 'r')
sys.stdout = open('expression.out', 'w')
# input_data = sys.stdin.readlines()
def input(): return sys.stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
def prime(n):
    p=2
    prm=[True for _ in range(n+1)]
    while p*p<=n:
        if prm[p]:
            for i in range(p*p,n,p):
                prm[i]=False
        p+=1
    return [i for i in range(2,n+1) if prm[i]]

def solve():
    m= int(input())
    n= int(input())
    a=inlt()
    prm=prime(max(a))
    # print(len(prm), prm)
    ans=defaultdict(int)
    for i in range(n):
        temp=a[i]
        while temp>1:
            for f in prm:
                if f > temp:
                    break
                while temp%f==0:
                    ans[f]+=1
                    temp//=f
    ret=[]
    perfect=True
    for i in ans:
        if ans[i]%m==0:
            ret.append([i,ans[i]//m])
        else:
            perfect=False
            break
    if perfect:
        print(1)
        if not ret:
            print(1,1)
        for i in ret:
            print(*i)
    else:
        print(0)

    

if __name__=="__main__": 
    solve()