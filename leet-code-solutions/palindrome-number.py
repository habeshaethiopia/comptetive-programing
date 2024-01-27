class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        i = len(x)

        return x==x[::-1]