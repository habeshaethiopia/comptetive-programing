n, m, k = map(int, input().split())
li = list(map(int, input().split()))
a = [0] * (n + 1)
op = []
for i in range(m):
    op.append(list(map(int, input().split())))
b = [0] * (m + 1)
for i in range(k):
    q = list(map(int, input().split()))
    b[q[0] - 1] += 1
    b[q[1]] -= 1
x = 0
for i, j in enumerate(b):
    x += j
    b[i] = x
b = b[:-1]
for i in range(m):
    a[op[i][0] - 1] += op[i][2] * b[i]
    a[op[i][1]] -= op[i][2] * b[i]
ans = [0] * n
for i in range(n):
    x += a[i]
    ans[i] += x
for i in range(n):
    ans[i] += li[i]
print(*ans)
