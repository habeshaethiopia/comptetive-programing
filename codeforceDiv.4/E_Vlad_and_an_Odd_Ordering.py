for _ in range(int(input())):
    n, k = map(int, input().split())
    print(k+n%k)
    