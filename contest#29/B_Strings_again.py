from sys import stdin
from collections import Counter


def input():
    return stdin.readline().strip()


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[: len(s)])


def invr():
    return map(int, input().split())


def solve():
    n, m, k = invr()
    a=[i for i in input()]
    b=[i for i in input()]
    a.sort()
    b.sort()
    l=0
    r=0
    ca=0
    cb=0
    c=""
    while l<n and r<m:
        # print(l,r)
        if (a[l]<b[r] and ca<k)or cb>=k :
            ca+=1
            c+=a[l]
            l+=1
            cb=0
        else:
            cb+=1
            c+=b[r]
            r+=1
            ca=0
    print(c)


    pass


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
