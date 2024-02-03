class Solution:
    def sortColors(self, array: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using selection sort
        size=len(array)
        for ind in range(size):
            min_index = ind
            for j in range(ind + 1, size):
                if array[j] < array[min_index]:
                    min_index = j
            (array[ind], array[min_index]) = (array[min_index], array[ind])
        