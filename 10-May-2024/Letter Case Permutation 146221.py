# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans=[]
        cnt=0
        letter=[]
        for i in range(len(s)):
            if  s[i]>='A' and s[i]<='z':
                cnt+=1 
                letter.append(i)
        print(cnt)
        n=len(bin(2**cnt-1)[2:])
        lis=[_ for _ in s]
        print(letter,n)
        for i in range(2**cnt):
            b=bin(i)[2:]
            b='0'*(n-len(b))+b
            temp=lis[:]
            print(b)
            for x in range(n):
                if b[x]=='1':
                    temp[letter[x]]=temp[letter[x]].swapcase()
                    print(temp)
            ans.append(''.join(temp))
            
        return ans