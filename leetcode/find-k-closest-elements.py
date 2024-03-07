class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # arr.sort(key=lambda y: abs(y-x))
        # return sorted(arr[:k])
        #An other implimentation
        ans=[]
        p=bisect_left(arr,x)
        l=p%len(arr)-1
        r=p
        if p==len(arr):
            l-=1
            r-=1
        while len(ans)<k:
            
            if abs(arr[l]-x)<=abs(arr[r]-x):
                ans.append(arr[l])
                l=(l-1)%len(arr)
            else:
                ans.append(arr[r])
                r=(r+1)%len(arr)
        return sorted(ans)
