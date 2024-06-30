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
    a=int(input())//1
    b=int(input())//2
    c=int(input())//4
    print( min(a,b,c)*7)

    
    pass
if __name__=='__main__':
    solve()