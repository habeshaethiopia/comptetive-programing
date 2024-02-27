class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rec(n,k)->int:
            if n==1:
                return 0
            value=2**(n-1)-1
            print(value)
            if k==value+1:
                return 1
            elif k<=value:
                return rec(n-1,k)
            elif k>value+1:
                return 1+ rec(n-1,2*value+1-k+1)
        s=rec(n,k)
        print(s)

        return '1' if s%2 else '0'
