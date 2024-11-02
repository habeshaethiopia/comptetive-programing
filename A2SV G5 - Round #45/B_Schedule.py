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
    a=inlt()
    pre=[]
    x=0

    for i in a:
        x+=i
        pre.append(x)
    cnt=Counter(pre)
    ans=0
    if pre:
        cnt[pre[-1]]=1
        for i in cnt:
            if i>0:
                if cnt[i]<=2:
                    ans+=cnt[i]
                else:
                    ans+=1
    print(ans)
if __name__=='__main__':
    solve()