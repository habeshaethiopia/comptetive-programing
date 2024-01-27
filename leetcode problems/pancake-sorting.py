class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        mx=len(arr)
        def flip(a, i):
            return a[:i][::-1]+a[i:]
        ans=[]
        while mx>0:
            idx=arr.index(mx)+1
            arr=flip(arr, idx)
            arr=flip(arr,mx)
            ans.extend([idx, mx])
            mx-=1
            arr=arr[:mx]
        return ans