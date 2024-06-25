# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n=len(s)
        temp=maxCost
        ans=0
        l=0
        for i in range(n):
            diff=abs(ord(s[i])-ord(t[i]))
            print(diff, temp)
            while diff>temp and i>=l:
                print(temp)
                temp+=abs(ord(s[l])-ord(t[l]))
                l+=1

            if diff<=temp:
                temp-=diff
                ans=max(ans,i-l+1)
                print(ans)
        return ans