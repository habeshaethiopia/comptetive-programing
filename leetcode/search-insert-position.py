class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        ans=len(nums)
        while h>=l:
            mid =(l+h)//2
            if nums[mid] >= target:
                h=mid-1
                ans=min(ans,mid)
            else:
                l=mid+1
            print(mid, l,h)
        return ans