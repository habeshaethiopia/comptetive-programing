class segmant_tree:
    def __init__(self, nums: List[int]):
        self.n=len(nums)
        self.arr=nums
        self.tree=[0] *(2*self.n)
        self.build()

    def build(self ):
        for i  in range(self.n):
            self.tree[i+self.n]=self.arr[i]
        for i in range(self.n-1,0,-1):
            self.tree[i]=self.tree[i<<1]+self.tree[i<<1|1]
    def update(self, index: int, val: int) -> None:
        self.arr[index]=val
        index+=self.n
        self.tree[index]=val
        while index>1:
            self.tree[index>>1]=self.tree[index]+self.tree[index^1]
            index>>=1
    def sumRange(self, left: int, right: int) -> int:
        left+=self.n
        right+=self.n+1
        ans=0
        while left<right:
            if left&1:
                ans+=self.tree[left]
                left+=1
            if right&1:
                right-=1
                ans+=self.tree[right]
            left>>=1
            right>>=1
        # print(self.tree)
        return ans


