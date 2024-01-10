class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mn=blocks[:k].count('W')
        print(mn)
        x=mn
        for i in range(k,len(blocks)):
            print(i)
            if blocks[i-k]=="W":
                mn-=1
            if blocks[i]=='W':
                mn+=1
            
            x=min(mn,x)
        return x
