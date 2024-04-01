# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        h=n
        l=1
        while h>=l:
            mid=(l+h)//2
            p=guess(mid)
            if p==1:
                l=mid+1
            elif p==-1:
                h=mid-1
            else:
                return mid
        return -1