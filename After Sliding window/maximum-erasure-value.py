class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left=0
        dic={}
        ans=0
        mx=0
        for i in range(len(nums)):
            if nums[i] in dic and dic[nums[i]]>=left:
                ans-=sum(nums[left:dic[nums[i]]+1])
                print(nums[left:dic[nums[i]]+1], end="=>")
                left=dic[nums[i]]+1
                print(left)
            dic[nums[i]]=i
            ans+=nums[i]
            print (ans)
            mx=max(mx,ans)

        return mx