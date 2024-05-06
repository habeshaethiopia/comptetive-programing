# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        temp=0
        for i in nums:
            temp^=i
        temp
        t=0
        for i in nums:
            if temp&-temp&i==0:
                t^=i
                
            
        
        
        return [temp^t, t]
        