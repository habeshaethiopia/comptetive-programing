from sys import stdin
from collections import Counter
from math import comb

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
    s=[]
    for i in range(n):
        s.append(input())
    ret=0
    pair=Counter(s)
    s=list(pair.keys())
    for i in range(len(s)):
        ans=0
        for j in range(i+1, len(s)):
            new=[i for i in  s[i]+s[j]]
            cnt=Counter(new)
            if len(new)%2:
                odd=[i for i in cnt if cnt[i]%2]
                if len(odd)==1:
                    ans+=1*pair[s[j]]
            else:
                odd=[i for i in cnt if cnt[i]%2]
                if len(odd)==0:
                    ans+=1*pair[s[j]]
        if pair[s[i]]>1:
            ret+=comb(pair[s[i]], 2)
        ret+=ans*pair[s[i]] 
        
    print(ret)
if __name__=='__main__':
    solve()