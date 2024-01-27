class UndergroundSystem(object):

    def __init__(self):
        self.new={}
        self.avg=defaultdict(list)
        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.new[id]=[stationName, t]

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """

        self.avg[(self.new[id][0],stationName )].append(t- self.new[id][1])

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        s = sum(self.avg[(startStation, endStation)])
        n= len(self.avg[(startStation, endStation)])
        return float(s)/n
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)