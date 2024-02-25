class Solution:
    def longestPalindrome(self, S: str) -> int:
        s=Counter(S)
        ans=0
        mx=0
        odd=False
        for i in s:
            if s[i]%2==0:
                ans+=s[i]
            else:
                ans+=s[i]-1 if odd else s[i]
                odd=True
            # print(ans)
        return ans