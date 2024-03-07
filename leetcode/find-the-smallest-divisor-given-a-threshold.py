class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        sm=sum(nums)
        L=1
        R=sm
        ans=1
        while L<=R:
            mid=(L+R)//2
            t=0
            for i in nums:
                t+=ceil(i/mid)
            if t>threshold:
                L=mid+1
            else:
                ans=mid
                R=mid-1
        return ans

