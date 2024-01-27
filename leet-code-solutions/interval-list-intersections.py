class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans=[]
        i=0
        j=0
        while i<len(firstList) and j<len(secondList):
            start=max(secondList[j][0],firstList[i][0])
            end=min(secondList[j][1],firstList[i][1])
            if start<=end:
                ans.append([start,end])
            if secondList[j][1]>firstList[i][1]:
                i+=1
            else:
                j+=1
        return ans