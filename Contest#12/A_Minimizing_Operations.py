for _ in range(int(input())):
    n=input()
    nums=list(map(int, input().split()))

    print(max(nums)-min(nums))