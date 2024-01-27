class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
      
        mx=0
        for x in ['T','F']:
            left=0
            ans=0
            c=k
            for right in range(len(answerKey)):
                if answerKey[right]==x:
                    c-=1
                if c<0:
                    if answerKey[left]==x:
                        c+=1
                    left+=1
                ans=max(ans,right-left+1)
            else:
                mx=max(ans,mx)
        return mx