n, m, k = map(int, input().split())
li = list(map(int, input().split()))
a = [0] * (n + 1)
op = []
for i in range(m):
    op.append(list(map(int, input().split())))
for i in range(k):
    q = list(map(int, input().split()))
    for x in range(q[0] - 1, q[1]):
        a[op[x][0] - 1] += op[x][2]
        a[op[x][1]] -= op[x][2]
x = 0
ans = [0] * n
for i in range(n):
    x += a[i]
    ans[i] += x
for i in range(n):
    ans[i] += li[i]
print(*ans)
