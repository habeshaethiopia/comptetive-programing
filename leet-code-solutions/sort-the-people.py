class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        name=dict(zip(heights, names))
        heights.sort(reverse=True)
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         if heights[i]<heights[j]:
        #             heights[i+1],heights[i]=heights[i],heights[i+1]
        return [name[i] for i in heights]
