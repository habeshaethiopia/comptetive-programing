class Solution:
    def shortestPalindrome(self, s: str) -> str:
        ans=0
        for i in range(len(s)+1):
            # finding the largest palindrom
            if s[:i]==s[:i][::-1]:
                ans=i
        
        return s[ans:][::-1]+s
        
