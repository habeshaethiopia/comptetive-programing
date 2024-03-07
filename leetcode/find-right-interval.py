class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic={tuple(intervals[i]):i for i in range(len(intervals))}
        intervals.sort(key=lambda x:x[0])
        ans=[-1]*len(intervals)
        for i ,val in enumerate(intervals):
            L=i
            R=len(intervals)-1
            while L<=R:
                mid=(L+R)//2
                print(val,intervals[mid])
                if val[1]<=intervals[mid][0]:
                    ans[dic[tuple(val)]]=dic[tuple(intervals[mid])]
                    R=mid-1
                else:
                    L=mid+1
        return ans