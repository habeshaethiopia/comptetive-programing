class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ctn=Counter(answers)
        ans=0
        for i in ctn:
            ans+=ceil(ctn[i]/(i+1))*(i+1)
            
        return ans

            