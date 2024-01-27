for _ in range(int(input())):
    n,m=map(int, input().split())
    a=list(map(int, input().split()))
    a.sort()
    if sum(a[1:])+a[-1] + n <=  m:
        print("YES")
    else:
        print("NO")