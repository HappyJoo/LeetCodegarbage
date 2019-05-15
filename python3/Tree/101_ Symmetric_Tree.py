# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val == right.val:
            return self.helper(left.left, right.right) and self.helper(left.right, right.left)
            
            
    # or maybe u prefer the function inside the function
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def helper(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            elif left.val == right.val:
                return helper(left.left, right.right) and helper(left.right, right.left)
        return helper(root.left, root.right)
