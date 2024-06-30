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
    s=input()
    l=0
    step=1
    ans=''
    while l<n:
        ans+=s[l]
        l+=step
        step+=1
    print(ans)
    
if __name__=='__main__':
    solve()