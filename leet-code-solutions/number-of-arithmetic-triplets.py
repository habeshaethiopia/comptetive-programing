class Solution:
    def arithmeticTriplets(self, nums: List[int], dif: int) -> int:
        p1=0
        p2=1
        ans=set()
        temp=set(nums)
        t=()
        for i in range(len(nums)-1):
           if nums[i]+dif in temp:
               if nums[i]+2*dif in temp:
                   ans.add((nums[i],nums[i]+dif,nums[i]+2*dif))
        
        return len(ans)

