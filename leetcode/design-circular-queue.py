class MyCircularQueue:

    def __init__(self, k: int):
        self.k=k
        self.f=-1
        self.l=-1
        self.stack=[0]*k
        self.s=0

    def enQueue(self, value: int) -> bool:
        if self.s<self.k:
            self.l=(self.l+1)%self.k
            if self.s==0:
                self.f=self.l
            self.stack[self.l]=value
            self.s+=1
            return True
        return False

    def deQueue(self) -> bool:
        if self.s>0:
            # self.stack[self.f]=0
            self.f=(self.f+1)%self.k
            self.s-=1
            return True
        return False

    def Front(self) -> int:
        if self.s>0:
            print(self.stack,self.s)
            return self.stack[self.f]
        return -1

    def Rear(self) -> int:
        if self.s>0:
            return self.stack[self.l]
        return -1

    def isEmpty(self) -> bool:
        return self.s==0

    def isFull(self) -> bool:
        return self.s==self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()