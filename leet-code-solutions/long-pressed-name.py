class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i,j=0,0
        while i < len(name) and j< len(typed):
            if name[i] == typed[j]:
                i+=1
                j+=1
            else:
                if i>0 and name[i-1]==typed[j]:
                    j+=1
                else:
                    return False
        if j<len(typed):
            while j<len(typed):
                if typed[j]!=name[i-1]:
                    return False
                j+=1
        if i<len(name):
            return False
        return True
