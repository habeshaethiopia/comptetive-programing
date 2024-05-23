# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        dummy=self.root
        for c in word:
            if dummy.children[ord(c)-ord('a')]:
                dummy=dummy.children[ord(c)-ord('a')]
                continue
            dummy.children[ord(c)-ord('a')]=TrieNode()
            dummy=dummy.children[ord(c)-ord('a')]
        dummy.is_end=True
            

    def search(self, word: str) -> bool:
        dummy=self.root
        for c in word:
            if dummy.children[ord(c)-ord('a')]:
                dummy=dummy.children[ord(c)-ord('a')]
                continue
            return False
        else:
            return dummy.is_end==True

    def startsWith(self, prefix: str) -> bool:
        dummy=self.root
        for c in prefix:
            if dummy.children[ord(c)-ord('a')]:
                dummy=dummy.children[ord(c)-ord('a')]
                continue
            return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)