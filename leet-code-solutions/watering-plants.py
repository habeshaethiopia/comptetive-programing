class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        temp=capacity
        sm=0
        for i in range(len(plants)):
            if temp >= plants[i]:
                sm+=1
                temp-=plants[i]
              
            else:
                sm+=i+i+1
                temp=capacity -plants[i]
            print(temp)
        return sm