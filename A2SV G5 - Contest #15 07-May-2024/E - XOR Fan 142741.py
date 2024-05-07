# Problem: E - XOR Fan - https://codeforces.com/gym/522079/problem/E

from sys import stdin


def input():
    return stdin.readline().strip()


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[: len(s) - 1])


def invr():
    return map(int, input().split())


def solve():
    n = int(input())
    a = inlt()
    s = input()
    q = int(input())
    pre = [0]
    x0 = 0
    total = 0
    for i in range(n):
        if s[i] == "0":
            x0 ^= a[i]
        total ^= a[i]
        pre.append(total)
    ans=[]
    for _ in range(q):
        qu = inlt()
        if qu[0]==2:
            if qu[1]==1:
                ans.append(total^x0)
            else:
                ans.append(x0)
        else:
            l,r=qu[1:]
            x0^= pre[r]^pre[l-1]
            # print('the pre',pre,pre[r-1],pre[l-2])
            # print("rev",l,r,x0)
    
            
    print(*ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
