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
    n,k,x=invr()
    buk=[i for i in range(1,k) if i != x ]
    def coin(sm):
        if sm == n:
            return 1
        for i in range(len(buk)):
            sm+=buk[i]
            if co

        
        
        

    pass
if __name__=='__main__':
    for i in range(int(input())):
        solve()