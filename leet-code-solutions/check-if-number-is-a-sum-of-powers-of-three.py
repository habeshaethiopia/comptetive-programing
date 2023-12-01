class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i = 1
        sum = n
        rem=0
        while sum > 0:
            rem = sum%3
            sum //=3
            if rem==2:
                return False
        return True

        