class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=[str(i) for i in nums]

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if int (nums[i]+nums[j])<int (nums[j]+nums[i]):
                    nums[i], nums[j]=nums[j], nums[i]
        ans=int("".join(nums))
        return str(ans)
        