n=int(input())
arr=list(map(int, input().split()))
ans=0
l=0
final=0

for r in range(1,n):
    if r-l == arr[r]-arr[l]:
        ans=r-l if arr[r]==1000 or r-l+1==n else r-l-1 
    else:
        l=r
        final+=ans
        ans=0
final+=ans
print(final)