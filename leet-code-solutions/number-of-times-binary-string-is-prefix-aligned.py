class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        # s=['0']*len(flips)
        c=0
        m=0
        for idx, i in enumerate(flips):
            # s[i-1]="1"
            m= max(i,m)
           
            if idx >= m-1:
                c+=1
        return c
