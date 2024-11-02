from sys import stdin
from math import log2


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
    n = int(input())
    c = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        elif n % 3 == 0:
            n = n // 3
            n *= 2
            n=int(n)

        elif n % 5 == 0:
            n //=5
            n *=4 
            n=int(n)
        else:
            break
        c += 1
    print(c if n==1 else -1)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
