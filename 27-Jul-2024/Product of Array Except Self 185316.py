# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x=1
        zero=0
        for i in nums:
            if i!=0:
                x*=i
            else:
                zero+=1
        a=[]
        for i in nums:
            if i==0 and zero==1 :
                a.append(x)
            elif zero==0:
                a.append(x//i)
            else:
                a.append(0)

        return a
       