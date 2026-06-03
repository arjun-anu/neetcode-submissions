# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = []
        stack.append((1, root))
        maxDepth = 0
        while stack:
            depth,node = stack.pop()
            maxDepth = max(depth,maxDepth)
            if node.left:
                stack.append((depth + 1, node.left))
            if node.right:
                stack.append((depth + 1, node.right))
        
        
        return maxDepth
        
    
