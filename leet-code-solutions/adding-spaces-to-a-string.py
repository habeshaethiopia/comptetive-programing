class Solution(object):
    def addSpaces(self, s, spc):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        result=[s[:spc[0]]]
        for i in range(1, len(spc)):
            result += [s[spc[i-1]:spc[i]]]
            
        result += [s[spc[-1]:]]
        return " ".join(result)
        