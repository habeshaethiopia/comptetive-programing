from bisect import bisect_right
n=int(input())
arr= list(map(int, input().split()))
arr.sort()
q=int(input())
for i in range(q):
    qi=int(input())
    print(bisect_right(arr, qi))