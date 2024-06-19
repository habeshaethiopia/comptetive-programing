# Problem: Find Xor-Beauty of Array - https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        ans=[0]*31
        for i in nums:
            b=bin(i)[2:]
            b='0'*(31-len(b))+b
            for x in range(31):
                if b[x]=='1':
                    ans[x]+=1
                    
        ret=''
        for i in range(31):
            if ans[i]%2:
                ret+='1'
            else:
                ret+='0'
        print(ans, ret)
        return int(ret,2)