# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nm=[-i for i in nums]
        heapify(nm)
        ans=0
        for i in range(k):
            x=heappop(nm)
            ans+=-x
            heappush(nm,ceil(x//3))
        return ans