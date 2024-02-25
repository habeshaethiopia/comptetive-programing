class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last={s[i]:i for i in range(len(s))}
        end=0
        ans=[]
        start=-1
        for i in range(len(s)):
            end=max(end,last[s[i]])
            if i==end:
                ans.append(end-start)
                start=end
                end=0
        return ans

            
