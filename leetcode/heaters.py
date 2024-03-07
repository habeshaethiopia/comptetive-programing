class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        L = 0
        houses.sort()
        heaters.sort()
        R = max(houses[-1], heaters[-1]) - min(houses[0], heaters[0])
        rad = R
        while L <= R:
            mid = (L + R) // 2
            i = 0
            j = 0
            while i < len(houses) and j < len(heaters):
                if heaters[j] - mid <= houses[i] <= heaters[j] + mid:
                    i += 1
                else:
                    j += 1
            if i<len(houses):
                L=mid+1
            else:
                rad=mid
                R=mid-1
        return rad