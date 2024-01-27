class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        count={}
        for root in paths:
            sub=root.split(' ')
            for i in range(1, len(sub)):
               div=sub[i]
               if "txt" in div:
                  inde=div.index(".txt")+4
                  lst = str(sub[0] + "/" + div[:inde])
                  count[div[inde:]]=count.get(div[inde:],[])+[lst]
        result=count.values()

        return [i for i in result if len(i)>1]