n = int(input())
a = []
p = []
for i in range(n):
    ai, pi = map(int, input().split())
    a.append(ai)
    p.append(pi)
stack = []
ans = 0
for i in range(len(a)):
    while stack and stack[-1] > p[i]:
        stack.pop()
    stack.append(p[i])
    ans += a[i] * stack[0]
    # print(stack)
print(ans)
