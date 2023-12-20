class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        newnum1=[i for i in nums if i<pivot]
        newnum2=[i for i in nums if i>pivot]
        newnum3=[i for i in nums if i==pivot]

        

        return newnum1+newnum3+newnum2