for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    path=[]
    ans=[]
    myset=set()
    arr.sort()
    for i in range(n):
        if arr[i+n]-arr[i]<x:
            print('NO')
            break
    else:
        print('YES')
