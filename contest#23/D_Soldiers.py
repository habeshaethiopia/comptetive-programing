from sys import stdin


def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
memo={0:1,1:1}
def factorial(n):
    if n in memo:
        return memo[n]
    
    else:
        memo[n]=n*factorial(n-1)
        return memo[n]
def solve():
    a,b=invr()
    
    print(a-1)
    pass
if __name__=='__main__':
    for _ in range(int(input())):
        solve()