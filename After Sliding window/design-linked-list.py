class Node:
    def __init__(self, value):
        self.v=value
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.mydic={}
        self.head=None
        
    def get(self, index: int) -> int:
        temp=self.head
        for _ in range(index):
            if temp==None:
                return -1
            temp=temp.next
        else:
            if temp:
                return temp.v
            else:
                return -1

    def addAtHead(self, val: int) -> None:
        temp=self.head
        self.head=Node(val)
        self.head.next=temp

    def addAtTail(self, val: int) -> None:
        temp=self.head
        if temp:
            while temp.next:
                temp=temp.next
            temp.next=Node(val)
        else:
            self.addAtHead(val)

    def addAtIndex(self, index: int, val: int) -> None:
        temp=self.head
        for _ in range(index-1):
            if temp==None:
                break
            temp=temp.next
        if index==0:
            self.addAtHead(val)
        else:
            if temp:
                t1=temp.next
                new=Node(val)
                temp.next=new
                new.next=t1

    def deleteAtIndex(self, index: int) -> None:
        temp=self.head
        if index==0 and temp:
            self.head=self.head.next
        for _ in range(index-1):
            if temp==None:
                break
            temp=temp.next
        
        t1=temp.next if temp else None
        if t1:
            t2=t1.next
            temp.next=t2
            del t1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)