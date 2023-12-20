class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i=0
        pair=[]
        while(True):
            pair.append([nums[2*i+1]]*nums[2*i])
            i +=1
            try:
                nums[2*i+1]
            except:
                break
        res=[]
        for lt in pair:
            res +=lt
        return res