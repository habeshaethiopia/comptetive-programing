class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        mx=-float('inf')
        for i in range(len(nums)-1, -1,-1):
            
            while stack and nums[stack[-1]]<nums[i] :
                mx=max(mx,nums[stack.pop()])
            stack.append(i)
            if stack and nums[stack[-1]]<mx:
                return True
        else:
            return False