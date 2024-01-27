class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result=[]
        
        for i in image:
            temp=[]
            for j in i[::-1]:
                if j==0:
                    j=1
                else:
                    j=0
                temp.append(j)
            result.append(temp)
        return result

                
