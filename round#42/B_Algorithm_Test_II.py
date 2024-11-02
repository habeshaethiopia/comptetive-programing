from sys import stdin
from collections import Counter, defaultdict

def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
def solve():
    q=int(input())
    ans=[]
    cnt=defaultdict(int)
    for _ in range(q):
        qu=input().split()
        if qu[0]== 'insert':
            x,y = int(qu[1]), int(qu[2])
            if (y,cnt[y]) in ans:
                ans.insert(ans.index(y,cnt[y]), x)
            else:
                ans.append(x)
        else:
            w=int(qu[1])
            if w in ans:
                ans.remove(w)
    print(*ans)
if __name__=='__main__':
    solve()