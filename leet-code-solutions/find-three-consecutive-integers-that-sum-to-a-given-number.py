class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num-3)%3==0:
            a = (num-3)//3
            return [a,a+1,a+2]
        else:
            return [] 