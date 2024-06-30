# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children=[None for _ in range(26)]
        self.is_end=False
class Trie:
    def __init__(self):
            self.root = TrieNode()
    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not current.children[idx]:
                current.children[idx] = TrieNode()
            current = current.children[idx]
        current.is_end = True
    def search(self, word):
        current = self.root
        c=0
        for ch in word:
            idx = ord(ch) - ord('a')
            # print(word,ch)
            if current.is_end:
                return word[:c] 
            
            if not current.children[idx]:
                break
            current = current.children[idx]
            c+=1
        
        return word 
  
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        T=Trie()
        for w in dictionary:
            T.insert(w)
        words=sentence.split()
        ans=''
        for w in words:
            ans+=' '+T.search(w)
        return ans[1:]
            

