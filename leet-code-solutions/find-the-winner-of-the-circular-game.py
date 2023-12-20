class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        frend=list(range(1,n+1))
        temp=0
        i=0
        remove=False
        while True and n > 1:
            temp+=1
            if temp == k:
                frend.remove(frend[i])
                temp=0
                remove=True
            if not remove:    
                i+=1
            remove=False
            if i > len(frend)-1:
                i=0
            if len(frend)==1:
                break
        return frend[0]

