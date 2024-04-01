
for _ in range(int(input())):
    def merge(left,right,n):
        ans=[]               
        if left[0] < right[0]:
            ans=left+right
        else:
            ans=right+left
            n+=1
        return ans, n
    def sorting(arr,l,r,n):
        if l==r:
            return [arr[l]], n
        mid=(l+r)//2
        left ,n=sorting(arr,l,mid,n)
        right ,n =sorting(arr,mid+1,r,n)

        return merge(left,right,n)
    
    m=int(input())
    p=list(map(int, input().split()))
    val,n=sorting(p,0,m-1,0)
    # print(val)
    if val==sorted(p):
        print(n)
    else:
        print(-1)
    