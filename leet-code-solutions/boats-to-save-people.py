class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        cnt=0
        l=0
        r=len(people) -1
        people.sort()
        while l<=r:
            print (people[l],people[r]) 
            if people[l]+people[r] <=limit:
                r-=1
                l+=1
            else:
                r-=1
            cnt+=1
        return cnt



