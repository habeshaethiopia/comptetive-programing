import math
for _ in range(int(input())):
    n,k = map(int, input().split())
    mx=max(n,k)
    mn=min(n,k)
    print(math.ceil(mx/mn))