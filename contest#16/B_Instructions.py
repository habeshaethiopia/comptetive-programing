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
        score=0
        pre=[[i+1+a[i], a[i]] for i in range(n)]

        print(pre)
        for i in range(n-1,-1,-1):
            if pre[i][0]<=n:
                pre[i][1]+=pre[pre[i][0]-1][1]
        ans=[i[1]for i in pre]
        print(max(ans)) 


        
if __name__=='__main__':
    solve()