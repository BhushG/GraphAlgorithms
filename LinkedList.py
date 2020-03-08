class Node:
    def __init__(self, val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def add(self,val):
        newNode = Node(val)
        if(self.head==None):
            self.head=newNode
        else:
            current=self.head
            while(current.next!=None):
                current=current.next
            current.next=newNode

    def reverse(self,prev,curr):
        if (curr.next == None):
            self.head = curr
            curr.next = prev
            return
        tmp = curr.next
        curr.next = prev
        self.reverse(curr, tmp)


    def traverse(self):
        current = self.head
        while(current!=None):
            print(str(current.val) + " ")
            current=current.next


if __name__ == "__main__":
    ls = LinkedList()
    ls.add(1)
    ls.add(2)
    ls.add(3)
    ls.add(4)
    ls.add(5)
    print("Original: ")
    ls.traverse()

    print("Reversed: ")
    ls.reverse(None, ls.head)
    ls.traverse()

