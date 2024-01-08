class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        c = 0
        sub = []
        for i in nums:
            if i==1:
                c += 1
            else:
                if c>0:
                    sub.append(c)
                    c=0
                sub.append(0)
        sub.append(c)
        if len(sub)==1:
            return sub[0] - 1
        if len(sub)==2: 
            return(max(sub))
        mx = 0
        for i in range(0,len(sub)-2,1):
            if i+2<=len(sub)-1:
                print("**")
                mx = max(mx, sub[i]+sub[i+2])
        return mx

