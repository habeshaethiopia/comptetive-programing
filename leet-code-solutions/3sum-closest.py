class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        c=float('inf')
        nums.sort()
        ans=0
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                if c>abs(nums[l]+nums[r]+nums[i]-target):
                    c=abs(nums[l]+nums[r]+nums[i]-target)
                    ans=nums[l]+nums[r]+nums[i]             
                # print(nums[i] ,nums[l],nums[r])
                if nums[l]+nums[r]+nums[i]>=target:
                    r-=1
                elif nums[l]+nums[r]+nums[i]<target:
                    l+=1
        return ans