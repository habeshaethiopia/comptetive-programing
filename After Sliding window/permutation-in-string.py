class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=l=len(s1)

        Str=dict(Counter(s1))
        count=defaultdict(int)
        if len(s2)<l:
            return False
        for i in range(l):
            count[s2[i]]+=1 
        
        for i in range(l,len(s2)):
            if count == Str:
                return True
            count[s2[i]]+=1
            print(count[s2[i-k]])
            if  count[s2[i-k]]>1:
                count[s2[i-k]]-=1
            else:
                del  count[s2[i-k]]
        else:
            if count == Str and len(s2)>=l:
                return True
            print(count, Str)
            return False