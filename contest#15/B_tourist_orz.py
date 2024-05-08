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
        n,z=invr()
        a=inlt()
        i=0
        # a.sort(key=lambda x:x^z,reverse=True)
        for i in range(n):
            a[i]=a[i]|z
        print(max(a))
    
if __name__=='__main__':
    solve()