# """
# Class: node
# methods: get, set, hasleftNode, has rightNode, isleftNode, isrightNode,isroot,isleaf
# """
# class Node:
#         #val,leftNode,rightNode
#     def __init__(self,val):
#         self.val = val
#         self.leftNode = None
#         self.rigtNode = None        
#     #get: return val
#     def get(self):
#         return self.val
#     #set: val = val
#     def set(self,val):
#         self.val = val
#     #hasleftNode: return leftNode
#     def hasLeftChild(self):
#         return self.leftNode

#     #hasrightchild: return rightchild
#     def hasRightChild(self):
#         return self.leftNode
#     #isLeaf
#     def isLeaf(self):
#         return not (self.leftNode or self.leftNode)

# class BST:
#     # root = None
#     def __init__(self):
#         self.root = None
#     # setRoot 
#     #input: val
#     def setRoot(self, val):
#         self.root = Node(val)

#     #insert
#     #input: val
#     #use insertNode
#     def insert(self,val):
#         if(self.root is None):
#             self.setRoot(val)
#         else:
#             self.insertNode(self.root, val)

#     #insertNode
#     #input: currentNode, val
#     def insertNode(self,currentNode,val):
#         """
#         if val <=currentnode.val
#             if currentndoe.leftchild
#                 insertnode(leftnode)
#             else insert to leftchild
#         else: val > currentnode.val
#             if currentnode.rightchild
#                 recursion rightnode,val
#             else 
#                 insert to rightnode
#         """
#         if val<=currentNode.val:
#             if currentNode.leftNode:
#                 self.insertNode(currentNode.leftNode,val)
#             else:
#                 currentNode.leftNode = Node(val)
#         elif val > currentNode.val:
#             if currentNode.rightNode:
#                 self.insertNode(currentNode.rightNode,val)
#             else:
#                 currentNode.rightNode = Node(val)
#     #find
#     #input val
#     #use findNode
#     def find(self,val):
#         return self.findNode(self.root,val)

#     #findNode
#     #input root, val
#     def findNode(self,node,val):
#         if node is None:
#             return False
#         elif node.val == val:
#             return True
#         elif node.val < val:
#             return self.findNode(node.leftNode,val)
#         else:
#             return self.findNode(node.rightNode,val)

#     def inOrder(self):
#         return self.inOrderTraveral(self.root)

#     def inOrderTraveral(self,node):
#         res = []
#         if node:
#             res = self.inOrderTraveral(node.leftNode)
#             res.append(node.val)
#             res = res + self.inOrderTraveral(node.rightNode)
#         return res

#     # def preOrder(self):
#     #     return self.preOrderTraveral(self.root)
#     # def preOrderTraveral(self,node):
#     #     if node:
#     #         print(node.val)
#     #         return self.preOrderTraveral(node.leftNode)
#     #         return self.preOrderTraveral(node.rightNode)

#     # def peek(stack): 
#     #     if len(stack) > 0: 
#     #         return stack[-1] 
#     #     return None
#     # # A iterative function to do postorder traversal of  
#     # # a given binary tree 
#     # def postOrderIterative(root): 
            
#     #     # Check for empty tree 
#     #     if root is None: 
#     #         return 
    
#     #     stack = [] 
        
#     #     while(True): 
            
#     #         while (root): 
#     #             # Push root's right child and then root to stack 
#     #             if root.right is not None: 
#     #                 stack.append(root.right) 
#     #             stack.append(root) 
    
#     #             # Set root as root's left child 
#     #             root = root.left 
            
#     #         # Pop an item from stack and set it as root 
#     #         root = stack.pop() 
    
#     #         # If the popped item has a right child and the 
#     #         # right child is not processed yet, then make sure 
#     #         # right child is processed before root 
#     #         if (root.right is not None and 
#     #             peek(stack) == root.right): 
#     #             stack.pop() # Remove right child from stack  
#     #             stack.append(root) # Push root back to stack 
#     #             root = root.right # change root so that the  
#     #                             # righ childis processed next 
    
#     #         # Else print root's data and set root as None 
#     #         else: 
#     #             ans.append(root.data)  
#     #             root = None
    
#     #         if (len(stack) <= 0): 
#     #                 break
    
class Node:
    def __init__(self, val,left =None,right=None):
        self.val = val
        self.leftChild = left
        self.rightChild = right
    
    def get(self):
        return self.val
    
    def set(self, val):
        self.val = val
    
    def __str__(self):
        string = str(self.val)
        if self.leftChild:  
            string += str(self.leftChild)
        else:          
            string += ""
        if self.rightChild: 
            string += str(self.rightChild)
        else:          
            string += ""
        return string
    def getChildren(self):
        children = []
        if(self.leftChild != None):
            children.append(self.leftChild)
        if(self.rightChild != None):
            children.append(self.rightChild)
        return children
        
class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if(val <= currentNode.val):
            if(currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif(val > currentNode.val):
            if(currentNode.rightChild):
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)

    def find(self, val):
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        if(currentNode is None):
            return False
        elif(val == currentNode.val):
            return True
        elif(val < currentNode.val):
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)

    def preOrder(self):
        return self.preOrderTraveral(self.root)
    def preOrderTraveral(self,node):
        if node:
            print(node.val)
            self.preOrderTraveral(node.leftChild)
            self.preOrderTraveral(node.rightChild)
