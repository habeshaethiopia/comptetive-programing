class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def fn(n):
            if n==1:
                return 0           
            return 2*fn(n//2) + (n//2)%2
        n4=fn(n)
        n5=fn(n+1)
        mod=10**9 + 7
        print(n4,n5,n)
        return (pow(4,n4,mod)*pow(5,n5,mod))%mod
        
