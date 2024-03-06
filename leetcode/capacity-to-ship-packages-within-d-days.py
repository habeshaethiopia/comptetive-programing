class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        mn=right
        while left<=right:
            mid=(left+right)//2
            D=1
            temp= 0
            for i in weights:
                temp+=i
                if temp>mid:
                    # print('temp',temp)
                    D+=1
                    temp=i
            # print(D, mid)
            if D <= days:
                mn=min(mn,mid)
                right=mid-1
            else:
                left=mid+1
        return mn