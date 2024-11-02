import sys
from collections import Counter,defaultdict
from heapq import heappop, heappush
sys.stdin = open('tourney.in', 'r')
sys.stdout = open('tourney.out', 'w')
# input_data = sys.stdin.readlines()
def input(): return sys.stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
def solve():
    n,m = invr()
    
    city=[0 for i in range(n+1)]
    mesg=defaultdict(int)
    for i in range(m):
        x,c=input().split()
        c=int(c)
        mesg[c]+=1
        if x=='N':
            city[c]=0
        else:
            city[c]=1
    mx=max(mesg.values())
    keys=len(mesg)
    print(*[i for i in range(1,n+1) if city[i]])
    print(*[i for i in range(1,n+1) if mesg[i]==mx])
    print(n-keys)
    

if __name__=="__main__": 
    solve()