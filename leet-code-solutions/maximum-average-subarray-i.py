class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans=[sum(nums[:k])]
        for i in range (k,len(nums),1):
           ans.append(ans[-1]-nums[i-k]+nums[i])
        return max(ans)/k