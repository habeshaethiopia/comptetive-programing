# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        """
        n=len(nums)
        dp=[0]*(1<<n)
        target=sum(nums)//k
        for bit in range(1,1<<n):
            temp=0
            for i in range(n):
                if bit>>i&1:
                    if temp:
                        temp+=nums[i]
            
            dp[bit]=(dp[bit-1]+temp)%k
            
            print(bit,temp)
        print(dp,target)
        return dp[-1]==0
        """
        nums.sort(reverse=True)
        target = sum(nums) // k
        visit = [False] * len(nums)
        n=len(nums)
        def dp(i, k, sm):
            if k == 0:
                return True
            if sm == target:
                return dp(0, k - 1, 0)
            for j in range(i, len(nums)):
                if visit[j] or sm + nums[j] > target or (j > 0 and nums[j] == nums[j-1] and not visit[j-1]):
                    continue
                visit[j] = True
                if dp(j + 1, k, sm + nums[j]):
                    return True
                visit[j] = False

            return False

        return dp(0, k, 0)
