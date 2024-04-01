class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        H = len(nums) - 1
        L = 0
        ans = [-1, -1]

        while H >= L:
            mid = (H + L) // 2
            if nums[mid] == target:
                ans[0]=mid
                H=mid-1
            elif nums[mid] < target :
                L = mid+1
            else:
                H=mid-1
        H = len(nums) - 1
        L = 0

        while H >= L:
            mid = (H + L) // 2
            if nums[mid] == target:
                ans[1]=mid
                L=mid+1
            elif nums[mid] < target :
                L = mid+1
            else:
                H=mid-1
        return ans
