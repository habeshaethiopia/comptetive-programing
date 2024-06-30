# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

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
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not current.children[idx]:
                current.children[idx] = TrieNode()
            current = current.children[idx]
        current.is_end = True

    def search(self, word: str) -> bool:
        current = self.root
        # print(current.children)
        
        def dfs(i,root):
            if i ==len(word):
                return root.is_end
            ch=word[i]
            idx = ord(ch) - ord('a')
            if ch=='.':
                # print(root.children)
                for r in root.children:
                    if r and dfs(i+1,r):
                        return True
            
                return False
            else:
                if not root.children[idx]:
                    return False
                root=root.children[idx]
                return dfs(i+1,root)
            
        return dfs(0,current)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)