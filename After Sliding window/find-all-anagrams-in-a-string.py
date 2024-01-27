class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        temp=Counter(p)
        k=len(p)
        wind=Counter(s[:k])
        if wind==temp:
                ans.append(0)
        for i in range(k,len(s)):
            print(wind)
            if wind[s[i-k]]>1:
                wind[s[i-k]]-=1
            else:
                del wind[s[i-k]]
            
            wind[s[i]]+=1
            if wind==temp:
                ans.append(i-k+1)
            
               

        return ans