class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        result=[]
        mx=0
        numright=nums.count(1)
        numleft=0
        for i in range(len(nums)+1):
            if numright+numleft>mx:
                mx=numright+numleft
                result=[]
            if numright+numleft==mx:
                result.append(i)
            if i<len(nums):
                if nums[i]==1:
                    numright-=1
                if nums[i]==0:
                    numleft+=1

        
        return result