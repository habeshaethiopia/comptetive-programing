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
        n,k=invr()
        s=''
        while len(s)!=n:
            for i in range(k):
                if len(s)>=n:
                    break
                s+=chr(97+i)
        print(s)
if __name__=='__main__':
    solve()