class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        path=[]
        ans=False
        a=[]
        def back(r,c,i):
            if i==len(word):
                return True

            if r<0 or c<0 or c==col or r==row or board[r][c]!=word[i] or [r,c] in path:
                return False
                
            path.append([r,c])
            ret = back(r+1,c,i+1) or back(r-1,c,i+1) or back(r,c+1,i+1) or back(r,c-1,i+1)
            path.pop()
            return ret


        for i in range(row):
            for j in range(col):
                if back(i,j,0):
                    return True
        return False
             


            
            
        print(a)
        back(0,0,0)
        return ans
               
       
            

