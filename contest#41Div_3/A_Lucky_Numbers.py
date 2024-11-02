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
    a=input().split()
    lucky=set(["4","7"])
    
    cnt=0
    c=0
    for i in a:
        for j in i:
            if j in lucky:
                c+=1
        # print(c)
        if c<=k:
            cnt+=1
        c=0
    print(cnt)

    pass
if __name__=='__main__':
    solve()