# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        minunfair=float('inf')
        chidren=[0]*k
        def backtrack(i):
            nonlocal minunfair
            if i==len(cookies):
                mx=max(chidren)
                minunfair=min(minunfair, mx)
                return

            for j in range(k):
                chidren[j]+=cookies[i]
                backtrack(i+1)
                chidren[j]-=cookies[i]
        if k<len(cookies):
            backtrack(0)
        else:
            return max(cookies)
        return minunfair
