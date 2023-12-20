class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x:x<0)
        n = len(nums)//2
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n])
            n +=1
        return result
