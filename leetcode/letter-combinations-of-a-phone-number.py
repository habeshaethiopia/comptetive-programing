class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        k = len(digits)
        dic={
            '2':'abc',
            '3':'def',
            '4': 'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
            
        }
      
        temp = []


        def com(cur):
            if len(temp) == k:
                x = "".join(temp)
                ans.append(x)
                return

            for i in dic[digits[cur]]:

                temp.append(i)
                com(cur+1)
                temp.pop()
        if k:
            com(0)
        return ans
