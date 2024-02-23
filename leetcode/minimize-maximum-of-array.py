class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        pri=[]
        x=0
        for i in nums:
            x+=i
            pri.append(ceil(x/(len(pri)+1)))
        return max(pri)