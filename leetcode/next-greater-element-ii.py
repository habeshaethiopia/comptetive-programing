class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums+=nums
        ans=[-1]*len(nums)
        stack=[]
        for i in range(len(ans)):
            while stack and nums[stack[-1]]<nums[i]:
                a=stack.pop()
                ans[a]=nums[i]
            stack.append(i)
            # print(stack)
        
        return ans[:n]
        