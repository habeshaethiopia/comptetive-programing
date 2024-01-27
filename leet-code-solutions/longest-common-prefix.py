class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre=""
        if not strs:
            return(pre)
        small = float("inf")
        for i in strs:
            small=min(len(i),small)

        for i in range(small):
            letter = strs[0][i]
            for j in strs:
                if letter != j[i]:
                    return strs[0][:i]
        return strs[0][:small]
        

               