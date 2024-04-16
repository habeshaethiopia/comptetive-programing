from math import gcd
for _ in range(int(input())):
    n=int(input())
    arr= list(map(int, input().split()))
    ans=0
    arr.sort()
    for i in range(n-2):
        for j in range(i+1,n-2):
                ans+=gcd(arr[i],arr[j])*3
    ans+=gcd(arr[n-3],arr[n-2])
    print(ans)