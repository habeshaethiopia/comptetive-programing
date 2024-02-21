class BrowserHistory:

    def __init__(self, homepage: str):
        self.home=homepage
        self.his=[homepage]
        self.curr=0

    def visit(self, url: str) -> None:
        vis=[]
        for i in range(self.curr+1):
            vis.append(self.his[i])
        self.curr=len(vis)
        self.his=vis+[url]

    def back(self, steps: int) -> str:
        print(self.curr)
        while steps and self.curr > 0:
            steps-=1
            self.curr-=1
        return self.his[self.curr]

    def forward(self, steps: int) -> str:
        while steps and self.curr < len(self.his)-1:
            steps-=1
            self.curr+=1
        # if self.curr >= len(self.his):
        #     self.curr-=1
        return self.his[self.curr] 
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)