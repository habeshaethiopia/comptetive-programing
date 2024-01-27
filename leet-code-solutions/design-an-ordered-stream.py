class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n=n
        self.counter = 1
        self.dic={}

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.dic[idKey] = value
        ans = []
        for i in range(self.counter, self.n+1):
            a= self.dic.get(i,[])
            if a == []:
                break
            else:
                ans.append(a)
                self.counter +=1
        
        return ans


        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)