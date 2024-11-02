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
    n=input()
    cnt=0
    while(len(n))>1:
        temp=0
        cnt+=1
        for i in range(len(n)):
            temp+=int(n[i])
        n=str(temp)
    print(cnt)
if __name__=='__main__':
    solve()