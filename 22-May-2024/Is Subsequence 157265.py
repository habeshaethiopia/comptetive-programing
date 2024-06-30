# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        x = 0
        for i in t:
            if len(s)>x and s[x] == i:
                x +=1
        if x == len(s):
            return True
        return False