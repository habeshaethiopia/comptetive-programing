class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        c=0
        k=0
        g.sort()
        s.sort()
        ans=0
        while c<len(g)and k<len(s):
            print(k, c , ans)
            if g[c] <= s[k]:
                ans+=1
                c+=1
                k+=1
            else:
                k+=1
        return ans
