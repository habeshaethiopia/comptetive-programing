t = int(input())
arr = list(map(int , input().split()))
arr.sort()

for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = 0-arr[i]
    

print(sum(arr))
