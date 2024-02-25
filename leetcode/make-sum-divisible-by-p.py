class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        sm=sum(nums)
        x=sm%p
        if x==0:
            return 0
        a={0:-1}
        n=len(nums)
        s=0
        for idx,val in enumerate(nums):
            s=(val+s) % p
            if (s-x)%p in a:
                if idx-a[(s-x)%p]<n:
                    n=idx-a[(s-x)%p]
            a[s]=idx
        return -1 if n==len(nums) else n