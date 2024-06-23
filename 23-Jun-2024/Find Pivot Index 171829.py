# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre=[]
        post=[]
        x=0
        for i in nums:
            x+=i
            pre.append(x)
        x=0
        for i in nums[::-1]:
            x+=i
            post.append(x) 
        post=post[::-1]
        for i in range(len(nums)):
            if post[i]==pre[i]:
                return i
        return -1
            