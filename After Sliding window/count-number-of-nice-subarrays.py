class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l=0
        ans=0
        cnt=0
        c={'odd':0}
        for i in range(len(nums)):
            if nums[i]%2:
                c['odd']+=1
                ans=0

            while c['odd']==k:
                ans+=1
                # print(nums[l:i+1])
                if nums[l]%2 :
                    c['odd']-=1
                l+=1
            cnt+=ans
        return cnt
