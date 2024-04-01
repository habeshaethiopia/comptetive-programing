class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        path=[]
        def permu():
            if len(nums)==len(path):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                permu()
                path.pop()
        permu()
        return ans