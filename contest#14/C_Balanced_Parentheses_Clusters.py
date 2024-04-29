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
    for _ in range(int(input())):
        n = 2 * int(input())
        s = input()

        root = {i: i for i in range(n)}
        size = [1] * n

        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    root[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    root[rootX] = rootY
                    size[rootY] += size[rootX]

        stack = []
        empty = []
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            elif stack:
                x=stack.pop()
                union(i,x)
        for i in range(1,n):
            if s[i-1]==')' and s[i]=='(':
                union(i,i-1)
        for i in range(n):
            root[i]=find(i) 

        # print(root)
        ans = 0
        for i in root:
            if root[i] == i:
                ans += 1
        print(ans)


if __name__ == "__main__":
    solve()
