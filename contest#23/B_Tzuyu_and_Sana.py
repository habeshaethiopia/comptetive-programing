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
    a,b=invr()
    x=a&b
    # print('x',x)
    print((a^x)+(b^x))
    
if __name__=='__main__':
    for _ in range(int(input())):
        solve() 