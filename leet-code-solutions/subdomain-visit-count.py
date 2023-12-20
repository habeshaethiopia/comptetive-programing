class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        my_dict={}
        for item in cpdomains:
            temp=item.split()
            domain = temp[1].split(".")
            temp2=""
            for i in range(len(domain)-1,-1,-1):
                temp2=domain[i]+'.'+temp2
                my_dict[temp2[:-1]] = my_dict.get(temp2[:-1], 0) + int(temp[0])
        result=[]
        for key in my_dict:
            value = my_dict[key]
            result.append(str(value)+ " "+ key)

            
        return result
