class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None


class BinarySearchTree:
    def __init__(self):
        self.root=None

    def addNode(self,root, newNode):
        if(newNode.val< root.val):
            if(root.left is None):
                root.left=newNode
                return
            self.addNode(root.left,newNode)
        else:
            if (root.right is None):
                root.right = newNode
                return
            self.addNode(root.right, newNode)


    def add(self,val):
        newNode = Node(val)
        if (self.root is None):
            self.root=newNode
        else:
            self.addNode(self.root, newNode)


    def inorder(self, node):
        if(not node==None):
            self.inorder(node.left)
            print(node.val)
            self.inorder(node.right)

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(3)
    bst.add(2)
    bst.add(7)
    bst.add(8)
    bst.inorder(bst.root)
