class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        l=0
        r=len(skill)-1
        chemo=[]
        sm=skill[l]+skill[r]
        fail=False
        while l<r:
            chemo.append((skill[l],skill[r]))
            if sm != skill[l]+skill[r]:
                return -1
            l+=1
            r-=1
        ret=0
        for i in chemo:
            ret+=i[0]*i[1]
        return ret


        