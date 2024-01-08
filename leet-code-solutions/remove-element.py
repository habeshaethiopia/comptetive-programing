class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
                count += 1
        return count
