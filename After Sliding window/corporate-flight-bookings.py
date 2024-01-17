class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        a=[0]*(n+1)
        for i in bookings:
            a[i[0]-1]+=i[2]
            a[i[1]]-=i[2]
        x=0
        ans=[]
        for i in a:
            x+=i
            ans.append(x)
        return ans[:n]