class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        mx=max(arr)
        idx=arr.index(mx)
        
        inc=arr[:idx]
        dec=arr[idx:]
        if (not (len(inc)>0 and len(dec)>1)) or len(arr)<1:
            return False
        
        for i in range(len(inc)-1):
            if inc[i] >= inc[i+1]:
                print("inc",inc[i],inc[i+1])
                return False
        for i in range(len(dec)-1):
            if dec[i] <= dec[i+1]:
                print(dec[i] , dec[i+1])
                return False
        return True
                
        