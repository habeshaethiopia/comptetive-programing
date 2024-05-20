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
    for _ in range(int(input())):
        n=int(input())
        print(n ,end=' ')
        for i in range(1,n):
            print(i ,end=' ')
        print()
    
if __name__=='__main__':
    solve()