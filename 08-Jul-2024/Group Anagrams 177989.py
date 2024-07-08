# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for s in strs:
            key=sorted([c for c in s])

            ans[tuple(key)].append(s)
        # print(ans)
        return ans.values()