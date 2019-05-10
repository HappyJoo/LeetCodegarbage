# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 中序遍历 Solution 1 inorder 
    # using a lot of space and time, not efficient.
    def isValidBST(self, root: TreeNode) -> bool:
        inorder = self.inorder(root)
        return inorder == sorted(set(inorder))
    
    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)


    # Solution 2 
    # Don't figure it out yet.
    # def isValidBST(self, root: TreeNode) -> bool:
    #     output = []
    #     self.inOrder(root, output)
    #     for i in range(1, len(output)):
    #         if output[i-1] >= output[i]:
    #             return False
    #     return True
    
    # def inOrder(self, root, output):
    #     if root is None:
    #         return  # Return None
        
    #     self.inOrder(root.left, output)
    #     output.append(root.val)
    #     self.inOrder(root.right, output)


    # Solution 3, still using inorder, but with less space
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev = None
        return self.helper(root)
    
    def helper(self, root):
        if root is None:
            return True
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)


    