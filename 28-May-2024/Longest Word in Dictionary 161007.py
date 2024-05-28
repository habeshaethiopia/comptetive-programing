# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

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
        
        for ch in word:
            idx = ord(ch) - ord('a')
            if not current.children[idx] or current.children[idx].is_end==False:
                print(word)
                return 0
            current = current.children[idx]
        return len(word)
            

class Solution:
    def longestWord(self, words: List[str]) -> str:
        T=Trie()
        words.sort()
        for w in words:
            T.insert(w)
        n=0
        ans=''
        for w in words:
            temp=T.search(w)
            print(temp)
            if n < temp:
                n=temp
                ans=w
        return ans