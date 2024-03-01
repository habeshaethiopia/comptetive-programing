for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    def mod(i, arr, pri):
        if i < len(arr):
            return 1

        if pri == 0:
            return 0
        else:
            return mod(i+1, arr, pri%arr[i+1])

    ans = mod(1, arr, arr[0] % arr[1])
    if ans==1:
        print("NO")
    else:
        print("YES")
