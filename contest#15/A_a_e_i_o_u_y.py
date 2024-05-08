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
    vowl=set(['a', 'e', 'i', 'o', 'u', 'y'])
    n=int(input())
    s=input()
    ans=s[0]
    for i in range(1,n):
        if ans[-1] in vowl and s[i] in vowl:
            continue
        # print(s[-1] , s[i])
        ans+=s[i]
    print(ans)
        

    
if __name__=='__main__':
    solve()