class Node:

    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item
        self.parent = None

    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.val) + " R:" + str(self.right)+')'

    def findCommonAncestor(self,n1,n2):
        arr = []
        while n1.parent != None:
            n1 = n1.parent
            arr.append(n1.val)
        while n2.parent !=None:
            n2 = n2.parent
            if n2.val in arr:
                return n2.val
        return None
    
    def findCommonAncestorTwo(self,n1,n2):
        difference = self.depth(n1) - self.depth(n2)
        first = None
        second = None
        if difference >0:
            first = n2.parent
            second = n1.parent
        else:
            first = n1.parent
            second = n2.parent
        while first != second and first != None and second != None:
            first = first.parent
            second = second.parent
        return first == None or second == None or first
    def goUpBy(self,node,difference):
        while difference >0 and node != None:
            node = node.parent
            difference -= 1
        return node
    def depth(self,node):
        depth = 0
        while node != None:
            node = node.parent
            depth += 1
        return depth

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
print(node.findCommonAncestor(node.left.left,node.right.right))
print(node.findCommonAncestorTwo(node.left.left,node.right.right))