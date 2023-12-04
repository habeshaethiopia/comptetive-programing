class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        mn=min(start,destination)
        mx=max(start,destination)
        total=sum(distance)
        sm=sum(distance[mn:mx])
        return (min(total-sm,sm))