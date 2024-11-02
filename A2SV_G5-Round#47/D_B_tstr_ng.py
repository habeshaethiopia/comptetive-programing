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
    n,k = invr()
    s=[i for i in input()]

    cnt=Counter(s[:k])
    print(cnt)
    for i in range(n-k):
        
        if  cnt['1']==cnt['0']:
            cnt[s[i]]-=1
            cnt[s[i+k]]+=1
        elif cnt['1']>cnt['0'] and cnt['?']>=cnt['1']-cnt['0']:
            cnt['0']+=cnt['1']-cnt['0']
            cnt['?']-=cnt['1']-cnt['0']
            if s[i]!= '?' or   cnt[s[i]]>0:
                cnt[s[i]]-=1
            else:
                cnt['0']-=1
            cnt[s[i+k]]+=1
            
        elif cnt['1']<cnt['0'] and cnt['?']>=cnt['0']-cnt['1']:
            cnt['1']+=cnt['0']-cnt['1']
            cnt['?']-=cnt['0']-cnt['1']
            if s[i]!= '?'or  cnt[s[i]]>0:
                cnt[s[i]]-=1
            else:
                cnt['1']-=1
            cnt[s[i+k]]+=1
        else:
            print('NO')
            break
        print(cnt)
        
    else:
        if  cnt['1']==cnt['0'] or cnt['?']==abs(cnt['0']-cnt['1']):
            print("YES")
        else:
            print('NO')

    

    
if __name__=='__main__':
    for _ in range(int(input())):
        solve()
