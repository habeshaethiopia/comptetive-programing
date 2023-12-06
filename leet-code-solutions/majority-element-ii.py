class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)//3
        snum = set(nums)
        result =[]
        for i in snum:
            if nums.count(i)>n:
                result.append(i)
        return result
