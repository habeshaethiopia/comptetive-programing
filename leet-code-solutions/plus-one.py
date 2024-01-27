class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for i in range(len(digits)):
            num+=digits[i]*10**(len(digits)-1-i)
            print(num)

        num=num+1
        result=[]
        while num>0:
            rem=num%10
            result.append(rem)
            num=num//10
        return result[::-1]
