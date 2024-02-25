l, r = map(int, input().split())
for i in range(l, r + 1):
    x = str(i)
    if len(x) == len(set([j for j in x])):
        print(x)
        break
else:
    print(-1)
