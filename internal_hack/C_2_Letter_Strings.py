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
    pair=[]
    for _ in range(n):
        i=input()
        pair.append(i)
    # pair.sort()
    cnt=Counter(pair)
    s=list(cnt.keys())
    # print(cnt,s)
    ans=0
    for i in range(len(s)):
        temp=0
        for j in range(i+1,len(s)):
            
            if (s[i][0]==s[j][0] and s[i][1]!=s[j][1]) or (s[i][0]!=s[j][0] and s[i][1]==s[j][1]):
                temp+=1*cnt[s[j]]
        ans+=cnt[s[i]]*temp
    print( ans)

        
if __name__=='__main__':
    for _ in range(int(input())):
        solve()