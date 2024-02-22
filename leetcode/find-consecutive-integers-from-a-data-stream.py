class DataStream:

    def __init__(self, value: int, k: int):
        self.v=value
        self.k=k
        self.queue=deque()
        self.c=0
        self.valid=0
        
    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num==self.v:
            self.valid+=1
        self.c+=1
        if self.c==self.k:
            if self.valid==self.k:
                if self.queue.popleft()==self.v:
                    self.valid-=1
                self.c-=1
                return True
            else:
                if self.queue.popleft()==self.v:
                    self.valid-=1
                self.c-=1
                return False
        else:
            return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)