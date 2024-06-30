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
        a=inlt()
        x=a[0]
        for i in a:
            x&=i
        print(x)
if __name__=='__main__':
    solve()