class Solution:
    def triangleNumber(self, nums: List[int]):
        nums.sort(reverse=True)
        l = 0
        r = 0
        ans = 0
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] < nums[l] + nums[r]:
                    # print(nums[i] ,nums[l], nums[r])
                    ans += r-l
                    l+=1
                else:
                    r -=1 
        return ans
