class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        ans=[i for i in palindrome]
        if len(ans)==1:
            return ''
        for i in range(len(ans)):
            if ans[i]!='a' and ans.count(ans[i])>1:
                ans[i]='a'
                break
        else:
            ans[-1]='b'
        return ''.join(ans)

            
        
