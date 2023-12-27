class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result=[]
        notin=[i for i in arr1 if i not in set(arr2)]
        notin.sort()
        arr1=Counter(arr1)
        for i in arr2:
            result+=[i]*arr1[i]
        return result + notin