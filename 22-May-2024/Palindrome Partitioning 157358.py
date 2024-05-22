# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, arr: str) -> List[List[str]]:
        ans=[]
        temp=[]
        def dp(i):
            if i>=len(arr):
                ans.append(temp[:])
                return 0
            for j in range(i,len(arr)):
                if arr[i:j+1]==arr[i:j+1][::-1]:
                    temp.append(arr[i:j+1])
                    dp(j+1)
                    temp.pop()
        dp(0)
        return ans
        
       
            

            
