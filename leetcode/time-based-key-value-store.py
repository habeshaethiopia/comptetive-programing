class TimeMap:

    def __init__(self):
        self.time = defaultdict(list)
        self.timestamp_prev=0

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append([value, timestamp])
        self.timestamp_prev=timestamp
    def get(self, key: str, timestamp: int) -> str:
        search=self.time[key]
        if not search:
            return '' 
        #search.sort(key=lambda x:x[1])
        L=0
        R=len(search)-1
        ans=''
        while L<= R:
            mid=(L+R)//2
            if search[mid][1]>timestamp:
                R=mid-1
            else:
                ans=search[mid][0]
                L=mid+1

        return ans
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
