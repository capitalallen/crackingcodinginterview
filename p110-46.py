class Node:

    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item
        self.parent = None

    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.val) + " R:" + str(self.right)+')'

    def inorderSuccessor(self,node):
        """
        case 1: node = None return null
        case 2: node.right != None return leftmost
        case 3: node.right == None q = node, x = q.parent while x !=null and q !=x.left
            return x
        """
        if node == None:
            return None
        if node.right != None:
            return self.leftMostChild(node.right)
        else:
            q = node
            x = q.parent
            while x != None and x.left != q:
                q = x
                x = x.parent
            return x
    def leftMostChild(self,node):
        """
        case 1: node = null return null
        case 2: while node.left !=null node == node.left
        return: node
        """
        if node == None:
            return None
        while node.left != None:
            node = node.left
        return node

node = Node(5)
node.left = Node(3)
node.right = Node(10)
node.left.parent = node
node.right.parent = node

node.left.left = Node(1)
node.left.right = Node(4)
node.left.left.parent = node.left
node.left.right.parent = node.left

node.right.left = Node(7)
node.right.right = Node(11)
node.right.left.parent = node.right
node.right.right.parent = node.right
print(node.leftMostChild(node))
print(node.inorderSuccessor(node))
print(node.inorderSuccessor(node.left.right))
print(node.left.right.parent.parent)
