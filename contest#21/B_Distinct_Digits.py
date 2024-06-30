from sys import stdin


def input(): return stdin.readline().strip()
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
memo={}
def solve():
    n=int(input())
    def back(n):
        if n in memo:
            return memo[n]
        if n<10:
            return n
        ans=float('inf')
        for i in range(1,10):
            curr=str(i)+str(back(n-i))
            # print(n,i,curr)
            temp=set([int(x) for x in curr])
            if sum(temp)==n:
                ans=min(ans,int(curr))
        memo[n]=ans
        return ans
    print(back(n))

    
if __name__=='__main__':
    for _ in range(int(input())):
        solve()