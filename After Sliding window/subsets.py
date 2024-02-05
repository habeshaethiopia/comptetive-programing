class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        for i in range(len(nums)+1):
            ans.extend([list(i) for i in itertools.combinations(set(nums),i)])
        return ans