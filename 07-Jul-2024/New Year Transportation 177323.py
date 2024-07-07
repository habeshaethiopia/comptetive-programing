# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

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


def dfs(graph, start_node):
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


def solve():
    n, t = invr()
    a = inlt()
    i = 0
    f = False
    while i < n :
        if i == t - 1:
            f = True
            break
        if i >= n-1:
            break
        else:
            i += a[i]
    if f:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()
