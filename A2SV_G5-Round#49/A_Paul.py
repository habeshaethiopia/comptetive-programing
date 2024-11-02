from sys import stdin
from collections import Counter

def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
def solve():
    s=input()
    cnt=Counter(s)
    n=0
    ans=0
    for i in cnt:
        if cnt[i]>1:
            ans+=1
        else:
            n+=1
    ans+=n//2
    print(ans)

if __name__=='__main__':
    for _ in range(int(input())):
        solve()
