# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(2) ]

class Trie:

    def __init__(self):
        self.root=TrieNode()

    def bin_(self, num:int)->str:
        bit=bin(num)[2:]
        bit='0'*(31-len(bit))+bit
        return bit
    def insert(self, num: int) -> None:
        bit=self.bin_(num)
        
        dummy=self.root
        for b in bit:
            if not dummy.children[int(b)]:
                dummy.children[int(b)]=TrieNode()
            dummy=dummy.children[int(b)]
    def xor(self, nums:list)->int:
        ans=0
        for num in nums:
            temp=''
            bit = self.bin_(num)
            dum=self.root
            for i in bit:
                if i =='0' and dum.children[1]:
                    dum=dum.children[1]
                    temp+='1'
                elif i =='1' and dum.children[0]:
                    dum=dum.children[0]
                    temp+='1'
                else:
                    temp+='0'
                    dum=dum.children[int(i)]
            print(temp)
            ans=max(ans, int(temp,2))
        return ans




        
            
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        sol=Trie()
        for i in nums:
            sol.insert(i)
        
        ans=0


        return sol.xor(nums)