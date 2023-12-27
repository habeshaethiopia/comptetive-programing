class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        # single= False
        multiple= False
        result=[]
        temp=""
        for i in source:
            s=0
            while s < len(i):
                if "/*" == i[s:s+2] and multiple==False:
                    s+=1
                    print("check /*")
                    multiple=True
                elif  i[s:s+2]=='//' and multiple==False:
                    print("check //")
                    break
                elif "*/" == i[s:s+2] and multiple==True:
                    s+=1
                    print("check */")
                    multiple=False
                elif multiple == False:
                    print("add to temp")
                    temp+=i[s]
                    # print(temp)
                s+=1
            if temp and multiple==False:
                result.append(temp)
                temp=""
            else:
                pass
            single=False
        return result