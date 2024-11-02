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
    n=int(input())
    s=Counter(i for i in input())
    keys=sorted(s.keys(),key=lambda x: s[x])
    ans=""
    for i in keys:
        ans+=i*s[i]

    print(ans)
    
        
if __name__=='__main__':
    for _ in range(int(input())):
        solve()