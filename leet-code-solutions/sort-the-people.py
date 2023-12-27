class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        name=dict(zip(heights, names))
        # heights.sort(reverse=True)
        for i in range(len(heights)):
            for j in range(len(heights)-i-1):
                if heights[j+1]>heights[j]:
                    heights[j+1],heights[j]=heights[j],heights[j+1]
        return [name[i] for i in heights]
