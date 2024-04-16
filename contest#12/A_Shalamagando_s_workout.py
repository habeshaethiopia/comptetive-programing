from sys import stdin


def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int, input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def solve():
    n=int(input())
    a=inlt()
    x=[0,0,0]
    for i in range(n):
        x[i%3]+=a[i]
    
    ans=zip(x,['chest',"biceps",'back'])
    print(dict(ans)[max(x)])
if __name__=='__main__':
    solve()