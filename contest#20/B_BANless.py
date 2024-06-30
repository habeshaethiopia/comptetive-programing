from sys import stdin


def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def solve():
    n=int(input())
    s='BAN'*n
    
    l=0
    r=3*n-1
    print(n-1)
    while l<r-1:
        print(l,r)
        r-=2
        l+=1
        if s[i]=='N':
            l+=1



    pass
if __name__=='__main__':
    for i in range(int(input())):
        solve()