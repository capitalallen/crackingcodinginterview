# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    return abs(self.getHeight(root.left)-self.getHeight(root.right))<2 and self.isBalanced(root.right) and self.isBalanced(root.left)

    def getHeight(self,root):
        if not root:
            return 0
        return 1 + max(self.getHeight(root.left),self.getHeight(root.right))


node = TreeNode(5)
node.left = TreeNode(3)
node.right = TreeNode(6)
print(isBalanced(node))

        