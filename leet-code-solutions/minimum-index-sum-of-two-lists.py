class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min = float("inf")
        result=[]
        for i in list1:
            if i in list2:
                index = list1.index(i) + list2.index(i)
                if min> index:
                    min = index
                    result = [i]
                elif min == index:
                    result.append(i)
        return result
        