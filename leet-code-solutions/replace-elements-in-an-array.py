class Solution(object):
    def arrayChange(self, nums, operation):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        index = {nums[i]:i for i in range(len(nums))}

        for  i in range(len(operation)):
            if operation[i][0] in index:
                x=index[operation[i][0]]
                nums[x]= operation[i][1]
                index[nums[x]]=x
        return nums