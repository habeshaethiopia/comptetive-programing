class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
        temp=sum([n for n in nums if n%2==0])
        result =[]
        # query = {i[1]:i[0] for i in queries}
        for val, idx in queries:
            if nums[idx]%2==0:
                temp -=  nums[idx]
            nums[idx] += val
            if nums[idx] % 2 ==0:
                temp += nums[idx]
            result.append(temp)
            
        return result