class Solution:
    def reverse(self, y: int) -> int:
        x=str(y)
        x= x[::-1]
        x= int(x)if y>=0 else 0-int(x[:-1]) 
        if x>=2**31 or x < -2**31:
            return 0
        else:
            return x