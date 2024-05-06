# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, x: int, y: int) -> int:
        
        # return a+b
        def two_complment(a):
            if a<0:
                a = (1 << 32) + a
            else:
                if (a & (1 << (31))) != 0:
                    a = a - (1 << 32)
            return a         
        a= two_complment(x)
        b= two_complment(y)
        print(a,b)
        while b:
            carry=(a&b)<<1
            a=a^b
            b=carry
        print(a-2*(1 << 32)) 
        ans=0
        if x>=0 and y>=0:
            ans=a
        else:
            pass
        return a if x>=0 and y>=0 else a-2*(1 << 32) if x<0 and y<0 else  a-(1 << 32) 

        

