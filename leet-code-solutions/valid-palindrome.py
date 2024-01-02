import re
class Solution(object):
    def isPalindrome(self, st):
        """
        :type s: str
        :rtype: bool
        """
        s=""
        for char in st:
            if char.isalpha() or char.isdigit():
                s += char.lower()
        print(s)
        a = [i for i in s]
        l = len(a)-1
        for i in range(len(a)):
            if a[l] != a[i]:
                return False
            l -=1
            if l==i:
                break
        return True         