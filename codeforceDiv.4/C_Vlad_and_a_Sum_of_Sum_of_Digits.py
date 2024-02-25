def sm(x):
    ans = 0
    while x != 0:
        r = x % 10
        x = x // 10
        ans += r
    return ans


myls = []
ans = 0
for i in range(1, 2*(10**5)+1):
            ans += sm(i)
            myls.append(ans)

for _ in range(int(input())):
    n = int(input())

    print(myls[n-1])
