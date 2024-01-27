class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sums=[]
        temp=0
        for i in nums:
            if i==1:
                temp+=1
            else:
                sums.append(temp)
                temp=0
        else:
            sums.append(temp)
        print(sums)
        return(max(sums))