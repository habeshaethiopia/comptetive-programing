n=int(input())
cord= list(map(int, input().split()))
speed=list(map(int, input().split()))
arr=list(zip(cord, speed))
arr.sort(key=lambda x:x[0])
#to check if the    the time is valid
# print(arr)
def helper(mid):
    
    mn=arr[0][0]+mid*arr[0][1]
    for i in arr:
        if mn>=i[0]:
            mn=min(mn, i[0]+i[1]*mid)
        else:
            can=i[0]-i[1]*mid
            if can>mn:
                return False
    return True

L=0
R=arr[-1][0]-arr[0][0]
ans=0
while L<=R:
    mid=(L+R)/2
    if helper(mid):
        R=mid-0.000001
        ans=mid
    else:
        L=mid+0.000001
print(ans)


        
