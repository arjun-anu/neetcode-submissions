# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: 
        # helper function to check whether given roots have the same tree
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right,subRoot.right))
        else:
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # since we recursively check both left and right side of root
        # if we reach the end (None) that means theres no more places to
        # look for 
        if root == None:
            return False
        # keep checking each portion using isSameTree helper function
        if self.isSameTree(root, subRoot):
            return True
        else:
            return ((self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot)))
        
        