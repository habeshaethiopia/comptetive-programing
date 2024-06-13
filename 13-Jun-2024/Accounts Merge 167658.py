# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        size = [len(i) for i in accounts]
        root = {i:i for i in range(len(accounts))}
        def find(x):
            if root[x] == x:
                return root[x]
            root[x] = find(root[x])  
            return root[x]
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    root[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    root[rootY]=rootX
                    size[rootY] += size[rootX]
    
        for i in range(len(accounts)):
            for j in range(i+1,len(accounts)):
                if accounts[i][0] == accounts[j][0]:
                    for k in accounts[i][1:]:
                        if k in accounts[j]:
                            union(i,j)
                            break
        print(root)
        for i in root:
            root[i]=find(root[i])
        ans=[]
       
        for child, parent in root.items():
            if  child!= parent:
                accounts[parent].extend(accounts[child][1:])
        for i in range(len(accounts)):
            if root[i]==i:
                
                ans.append(accounts[i][:1]+sorted(list(set(accounts[i][1:]))))
        return ans
