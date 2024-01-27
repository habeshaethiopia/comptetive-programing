class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S=Counter(s)
        T=Counter(t)
        print(S,T)
        if S==T :
            return True
        else:
            return False
       