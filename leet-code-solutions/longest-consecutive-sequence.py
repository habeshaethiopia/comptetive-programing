class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = list(set(nums))
        num.sort()
        pos=[]
        count =0
        if len(nums) > 0:
            count =1
        for i in range(len(num)-1):
            if num[i+1]-num[i] ==1:
                count +=1
            else:
                pos.append(count)
                count = 1
        else:
            pos.append(count)
        return max(pos)
                