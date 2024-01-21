class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        x=0
        for i in nums:
            x+=i
            ans.append(x)
        return ans