class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        path=[]
        nums.sort()
        n=0
        def subset(curr):
            nonlocal n
            n+=1
            if len(path)>len(nums):
                return
            if path in ans:
                return
            else:
                ans.append(path[:])
               
            k=None
            for i in range(curr, len(nums)):
                if k==nums[i]:
                    continue
                path.append(nums[i])
                subset(i+1)
                k=path.pop()
        subset(0)
        print(n)
        return ans
