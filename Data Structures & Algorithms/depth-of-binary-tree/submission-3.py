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
        maxDepth = 0
        stack.append((1, root))
        while stack:
            depth, node = stack.pop()
            if node.left:
                stack.append((depth+1, node.left))
            if node.right:
                stack.append((depth+1, node.right))
            maxDepth = max(maxDepth, depth)
        return maxDepth
    
