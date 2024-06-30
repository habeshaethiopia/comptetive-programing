# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        d= defaultdict(set)
        n=len(s)
        def helper(i,j):
            while i>=0 and j<n and s[i]==s[j]:
                d[i].add(j)
                i-=1
                j+=1
        for i in range(n):
            helper(i,i)
            helper(i,i+1)
        print(d)
        @lru_cache(None)
        def dfs(i):
            if i==n:
                return 0
            temp=[]
            for j in range(i,n+1):
                if j in d[i]:
                    temp.append(dfs(j+1)+1)
            return min(temp)
        return dfs(0)-1
