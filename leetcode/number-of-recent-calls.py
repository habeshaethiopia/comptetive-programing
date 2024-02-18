class RecentCounter:

    def __init__(self):
        self.recent=[]

    def ping(self, t: int) -> int:
        self.recent.append(t)
        c= 0
        for i in self.recent:
            if i <= t and i>= t-3000:
                c+=1
        return c

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)