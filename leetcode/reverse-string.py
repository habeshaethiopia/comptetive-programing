class Solution:
    def __init__(self):
        self.l=0
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        '''
       #using iteration
        i=0
        j=len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        '''
        if self.l>len(s)//2-1:
            pass
        else:
            s[self.l],s[0-self.l-1]=s[0-self.l-1],s[self.l]
            self.l+=1
            self.reverseString(s)
            