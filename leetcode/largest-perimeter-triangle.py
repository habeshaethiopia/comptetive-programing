class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            n=nums[i:i+3]
            print(n)
            if n[0] + n[1] > n[2] and n[2] + n[1] > n[0] and n[0] + n[2] > n[1]:
                return sum(n)
        else:
            return 0