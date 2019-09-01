# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root == None:
        return True
    else:
        if not root.left or not root.left:
            return False
        isBalanced(root.left)
        isBalanced(root.right)
node = TreeNode(5)
node.left = TreeNode(3)
node.right = TreeNode(6)
print(isBalanced(node))

        