i = int(input())
for l in range(i):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key=lambda li : li%2, reverse=True)
    print(*a)