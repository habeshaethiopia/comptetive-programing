class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        ans=0
        tp=defaultdict(int)
        for i in range(len(fruits)):
            tp[fruits[i]]+=1
            while len(tp)> 2:
                if tp[fruits[l]]>1:
                    tp[fruits[l]]-=1
                else:
                    del tp[fruits[l]]
                l+=1
            ans=max(ans,i-l+1)
            # print(tp,l,ans)
            
        return ans
                
