class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
       ans=[]
       c=0
       for i in nums:
           c=0
           for j in nums:
               if i>j:
                   c+=1
           ans.append(c)
       return (ans)




        