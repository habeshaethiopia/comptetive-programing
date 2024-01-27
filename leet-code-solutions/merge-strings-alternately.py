class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge=""
        w1=0
        w2=0
        for i in range(max(len(word1),len(word2))):
            
            if(w1)<len(word1):
                merge+=word1[w1]
                w1+=1
            if(w2)<len(word2):
                merge+=word2[w2]
                w2+=1
        return merge
