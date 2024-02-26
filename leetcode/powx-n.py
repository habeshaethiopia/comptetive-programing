class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n*=-1
        if n==0:
            return 1
        if n==1:
            return x
        if n%2==0:
            a=self.myPow(x, n//2)
            return a*a
        if n%2==1:
            return x*self.myPow(x, n-1)
        
