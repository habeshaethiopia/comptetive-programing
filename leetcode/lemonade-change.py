class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hand=defaultdict(int)
        for i in bills:
            if i ==5:
                hand[5]+=1
            elif i==10:
                if hand[5]:
                    hand[5]-=1
                    hand[10]+=1
                else:
                    return False
            else:
                if hand[10] and hand[5]:
                    hand[5]-=1
                    hand[10]-=1
                elif hand[5] > 2:
                    hand[5]-=3
                else:
                    return False
        return True
                    

