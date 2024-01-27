class Solution:
    def increasingTriplet(self, num: List[int]) -> bool:
        result={}
        count=0
        y= float("inf")
        
       
        x=num[0]
        xf=False
        for i in range(1,len(num)):
            if x>=num[i]:
               x=num[i]
            elif y>= num[i]:
                y=num[i]
            else:
                return True

        return False
        