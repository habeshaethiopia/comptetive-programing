class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keybord=["qwertyuiop","asdfghjkl","zxcvbnm"]
        result=[]
        for row in keybord:
            for word in words:
                count = 0
                word_lower = word[:].lower()
                for letter in word_lower:
                    if letter in row:
                        count += 1
                if count == len(word):
                    result.append(word)
        return result
