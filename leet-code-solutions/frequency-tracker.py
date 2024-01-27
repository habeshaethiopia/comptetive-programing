class FrequencyTracker(object):

    def __init__(self):
        self.frequency=defaultdict(int)
        self.f=defaultdict(int)

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        if self.frequency[number]:
            if self.f[self.frequency[number]] > 0:
                self.f[self.frequency[number]]-=1
        self.frequency[number] += 1
        self.f[self.frequency[number]]+=1
        

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        if self.frequency[number]>0:
            self.f[self.frequency[number]]-=1
            self.frequency[number]-=1
            self.f[self.frequency[number]]+=1

    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        
        if self.f[frequency]:
            return True
        else:
            return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)