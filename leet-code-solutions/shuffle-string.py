class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        restorted=["" for i in s]
        idx=0
        for i in indices:
            restorted[i]=s[idx]
            idx+=1
        return "".join(restorted)