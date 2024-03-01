for _ in range(int(input())):
    n= int(input())
    arr= list(map(int, input().split()))
    ans=0
    for i in arr:
        ans+=abs(i)
    print(ans)