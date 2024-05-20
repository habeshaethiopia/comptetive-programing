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
    a=inlt()
    new=[(a[i],i)for i in range(n)]
    new.sort()
    for i in range(n//2):
        print(new[i][1]+1,new[n-i-1][1]+1)
if __name__=='__main__':
    #for i in range(int(input())):
    solve()