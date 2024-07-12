# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        s=[]
        pre=chars[0]
        c=1
        for i in range(1,len(chars)):
            if pre==chars[i]:
                c+=1
            else:
                s.append(pre)
                pre=chars[i]

                if c>1:
                    s.append(c)
                    C=1
                if i== len(chars)-1:
                    break
        else:
            s.append(pre)
            if c>1:
                s.append(c)
            print(s)
        return len(s)
