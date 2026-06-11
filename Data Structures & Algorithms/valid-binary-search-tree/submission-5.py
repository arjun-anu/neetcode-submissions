# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        if root == None or (root.left == None and root.right == None):
            return True
        elif (not root.left or (root.left and root.left.val < root.val)) and  (not root.right or (root.right and root.right.val > root.val)):
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False
        '''
        def valid(node, left, right):
            if not node:
                return True
            if not(left < node.val < right):
                return False
            else:
                return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root,float("-inf"),float("inf"))

        