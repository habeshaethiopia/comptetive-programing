class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        reach=1
        i=0
        ans=0
        while(reach < n+1):
            if i<len(nums) and reach >= nums[i]:
                reach+=nums[i]
                i+=1
            else:
                ans+=1
                reach *=2
        return ans