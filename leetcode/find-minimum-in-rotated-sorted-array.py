class Solution:
    def findMin(self, nums: List[int]) -> int:
        L=0
        R=len(nums)-1
        ans=float('inf')
        while L<=R:
            mid=(L+R)//2
            ans=min(ans, nums[R], nums[mid], nums[L])
            if nums[L]>nums[R]:
                if nums[mid]>nums[L]:
                    L=mid+1
                else:
                    R=mid-1
            else:
                break
                return nums[L]
            # print(ans)
        return ans

