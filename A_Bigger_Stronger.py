
for i in range(int(input())):

    n = int(input())
    num=list(map(int, input().split()))

    if n == len(set(num)):
        print("YES")
    else:
        print("NO")
