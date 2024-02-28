class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s,index):
            string=''
            k=0
            while index<len(s):
                if s[index].isdigit():
                    k=k*10+ int(s[index])
                    print(k)
                elif s[index]=='[':
                    index,st=decode(s,index+1)
                    string+=st*k
                    k=0
                elif s[index]==']':
                    return index,string
                else:
                    string +=s[index]
                index+=1
            return index, string
        i,ans=decode(s, 0)


        
        return ans

