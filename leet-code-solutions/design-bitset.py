class Bitset:
    def __init__(self, size: int):
        self.bit=["0" for _ in range(size)]
        self.bitflip= ["1" for _ in range(size)]
        self.cnt=0
        self.size=size

    def fix(self, idx: int) -> None:
        if self.bit[idx] =='0':
            self.bit[idx] ='1'
            self.bitflip[idx] = '0'
            self.cnt+=1

    def unfix(self, idx: int) -> None:
        if self.bit[idx] =='1':
            self.bit[idx] = '0'
            self.bitflip[idx] = '1'
            self.cnt-=1


    def flip(self) -> None:
       

        # for i in range(self.size):
        #     if self.bit[i]=='0':
        #         self.bit[i]='1'
        #     else:
        #         self.bit[i]='0'
        # swap(self.bit, self.bitflip)
        temp = self.bit
        self.bit=self.bitflip
        self.bitflip=temp
        self.cnt = self.size-self.cnt

    def all(self) -> bool:
        return self.cnt == self.size

    def one(self) -> bool:
        return self.cnt>0
        

    def count(self) -> int:
        return self.cnt

    def toString(self) -> str:
        return "".join(self.bit)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()