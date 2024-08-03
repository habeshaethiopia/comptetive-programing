# Problem: Search in Rotated Sorted Array II - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        m=nums[0]
        pivot=0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                pivot=i+1
                break
            
            
        nums=nums[pivot:]+nums[:pivot]
        x=bisect_left(nums,target)
        # print(x,nums, pivot)
        return nums[x%len(nums)]==target
        