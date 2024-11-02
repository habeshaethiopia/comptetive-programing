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
    n=int(input())-1
    alis=1
    bob= 0
    c=1
    # print(n,"====")
    while n>0:
        c+=1
        n-=c
        if n>=0:
            bob+=c
        else:
            bob+=c+n
            break
        # print(n,c)

        c+=1
        n-=c
        if n>=0:
            bob+=c
        else:
            bob+=c+n
            break
        # print(n,c)

        c+=1
        n-=c
        if n>=0:
            alis+=c
        else:
            alis+=c+n
            break
        # print(n,c)
            
        c+=1
        n-=c
        if n>=0:
            alis+=c
        else:
            alis+=c+n
            break
        # print(n,c, "====")
    print(alis,bob)
if __name__=='__main__':
    for  i in range(int(input())):
        solve()