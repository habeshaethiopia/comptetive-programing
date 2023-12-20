class Solution:
    def totalMoney(self, n: int) -> int:
        qu=n//7
        rem=n%7
        w_sum=qu*(56+(qu-1)*7)//2
        d_sum= rem*(2*(qu+1)+rem-1)//2
        return w_sum+d_sum if rem else w_sum