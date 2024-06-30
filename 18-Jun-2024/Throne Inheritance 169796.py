# Problem: Throne Inheritance - https://leetcode.com/problems/throne-inheritance/

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.suc=[kingName]
        self.parent=defaultdict(list)
        self.p={}
        self.dead=set()
    def birth(self, parentName: str, childName: str) -> None:
        self.parent[parentName].append(childName)
        self.p[childName]=parentName

    def death(self, name: str) -> None:
        self.dead.add(name)
    def getInheritanceOrder(self) -> List[str]:

        ans=[]
        stack=self.suc[:]
        while stack:
            x=stack.pop()
            if x not in self.dead:
                ans.append(x)
            for i in self.parent[x][::-1]:
                    stack.append(i)
        return ans
                

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()