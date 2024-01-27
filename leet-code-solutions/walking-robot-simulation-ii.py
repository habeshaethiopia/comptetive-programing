class Robot:

    def __init__(self, width: int, height: int):
        self.width=width-1
        self.height= height-1
        self.pos=[0,0]
        self.dir="East"
        self.parameter=2*self.width +2*self.height

    def step(self, num: int) -> None:
        # if self.pos[0]<self.width and self.pos[0]+num<self.width:
        #     self.pos[0]+=num
        #     self.dir= "East"
        # elif (self.pos[0]>=self.width or  self.pos[0]+num<self.width) and self.pos[1]<self.height and  self.pos[1]+num<self.height:
        #     self.pos[1]+=num
        #     self.dir="North"
        # elif self.pos[0] + num>=self.width and self.pos[1]+num>= self.height:
        #     self.pos[0]-=num
        #     self.dir="West"
        # elif 
        num=num% self.parameter
        for i in range(num):
            if self.pos==[0,0]:
                self.dir="East"
            elif self.pos==[self.width,0]:
                self.dir="North"
            elif self.pos==[self.width,self.height]:
                self.dir="West"
            elif self.pos == [0,self.height]:
                self.dir="South"

            if self.dir=="East":
                self.pos[0]+=1
            elif self.dir=="West":
                self.pos[0]-=1
            elif self.dir=="North":
                self.pos[1]+=1
            elif self.dir=="South":
                self.pos[1]-=1
        if self.pos==[0,0]:
            self.dir="South"
            

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dir


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()