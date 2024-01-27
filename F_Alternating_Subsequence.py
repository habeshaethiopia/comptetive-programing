t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    larg = a[0]
    sum = 0
    for i in range(1, n):
        if a[i] > 0:
            if larg > 0:
                larg = max(larg, a[i])
            else:
                sum += larg
                larg = a[i]
        else:
            if larg < 0:
                larg = max(larg, a[i])
            else:
                sum += larg
                larg = a[i]
    sum += larg
    print(sum)