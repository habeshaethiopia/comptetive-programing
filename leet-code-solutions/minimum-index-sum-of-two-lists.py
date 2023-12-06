class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min = float("inf")
        result=[]
        for item in list1:
            if item in list2:
                index_sum = list1.index(item) + list2.index(item)
                if min > index_sum:
                    min = index_sum
                    result = [item]
                elif min == index_sum:
                    result.append(item)
        return result
        