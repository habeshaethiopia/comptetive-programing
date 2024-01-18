class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        def check(arr, key,x):
            l=0
            ans=0
            for i in range(len(arr)):
                if arr[i]!=key:
                    x-=1
                while x<0:
                    if arr[l]!=key:
                        x+=1
                    l+=1
                ans=max(ans, i-l+1)
            return ans
        return check(nums,1,k)
                



'''
        ans=[]
        patt=[]
        c=0
        c0=0
        for i in nums:
            if i==1:
                c+=1
                if c0>0:
                   ans.append(c0)
                   patt.append(0)
                   c0=0
            else:
                c0+=1
                if c>0:
                   ans.append(c)
                   patt.append(1)
                   c=0
        if c0>0:
            ans.append(c0)
            patt.append(0)
            c0=0
        if c>0:
            ans.append(c)
            patt.append(0)
            c=0
        print(ans)

        for i in patt:
            if i==1:
              pass  
        return 0
        '''