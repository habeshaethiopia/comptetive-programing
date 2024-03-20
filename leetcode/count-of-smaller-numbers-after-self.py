class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n={(val,i):0 for i,val in enumerate(nums)}
        def merge(left,right):
            nonlocal n
            l=0
            r=0
            ans=[]
            pri=[0]*len(left)               
            while l<len(left) and r<len(right):
                # print(left,right)
                if left[l][0] <= right[r][0]:
                    ans.append(left[l])
                    l+=1
                else:
                    # for i in range(l,len(left)):
                    #     n[left[i]]+=1
                    pri[l]+=1
                    ans.append(right[r])
                    r+=1
            x=0
            prifix=[]
            for i in pri:
                x+=i
                prifix.append(x)
            for i in range(len(left)):
                n[left[i]]+=prifix[i]
            ans.extend(left[l:])
            ans.extend(right[r:])
            return ans
        def sort(arr,l,r):
            if l==r:
                # print(r)
                return [(arr[l], l)]
            mid=(l+r)//2
            left=sort(arr,l,mid)
            right=sort(arr,mid+1,r)

            return merge(left,right)

        print(sort(nums,0,len(nums)-1))
        print(n)
        return [n[(val,i)] for i,val in enumerate(nums)]