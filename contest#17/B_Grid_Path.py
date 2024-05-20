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
    n,m,k=invr()
    # curr=[0]*m
    # prev=[0]*m
    # curr[0]=1
    # for i in range(n):
    #     for j in range(1,m):
    #         curr[j]=curr[j-1]+prev[j]
    #     prev=curr
    #     # print(curr)
    #     curr=[0]*m
    #     curr[0]=1
    # print(prev[-1])

    print('YES' if n*m-1==k else 'NO')

    
    pass
if __name__=='__main__':
    for i in range(int(input())):
        solve()