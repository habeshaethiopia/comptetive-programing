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
        s=input()
        n=len(s)
        if len(s)%2==0 and s[:n//2]*2==s:
            print('YES')
            
        else:
            print('NO')
if __name__=='__main__':
    solve()