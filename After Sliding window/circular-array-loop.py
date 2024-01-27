class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        priv=0
        for i in range(n):
            slow = fast = i
            x=i
            cont=False
            while x< len(nums) and x>=0:
                if nums[i]>=0:
                    if nums[x]<0:
                        cont=True
                        break
                else:
                    if nums[x]>0:
                        cont=True
                        break
                x+=nums[x]
            if cont:
                continue
            while True:
                slow = (slow + nums[slow]) % n
                
                fast = (fast + nums[fast]) % n
                priv=nums[fast]
                fast = (fast + nums[fast]) % n

                if slow == fast:
                    break
                if nums[i] * nums[slow] <= 0 or nums[i] * nums[fast] <= 0:
                    break
                if slow == (slow + nums[slow]) % n:
                    break
            
            if slow == fast and slow != (slow + nums[slow]) % n:
                return True
        return False