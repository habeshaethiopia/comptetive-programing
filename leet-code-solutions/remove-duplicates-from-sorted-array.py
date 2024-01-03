class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        l1=1
        for i in range(len(nums)):
            if l1< len(nums) and nums[l]==nums[l1]:
                nums.remove(nums[l])

            else:
                l1+=1
                l+=1
                    
        print(nums)
        return len(nums)