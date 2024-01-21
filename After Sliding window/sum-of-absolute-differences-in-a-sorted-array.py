class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        sm=[]
        n=len(nums)
        x=0
        for i in nums:
            x+=i
            sm.append(x)
        
        print(sm)
        ans=[]
        for i in range(n):
            l=nums[i]*(i+1)-sm[i]
            r=sm[-1]-sm[i] - nums[i]*(n-i-1)
            print(l,r)
            ans.append(l+r)
        return ans
        

        