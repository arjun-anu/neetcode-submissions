# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if its an empty stack depth = 0
        if not root:
            return 0
        maxDepth = 0
        # stack to store incoming nodes and apply logic to latest ones
        stack = []
        #appending in a tuple format cause we need both nodes and depth at each node
        stack.append((1,root)) 

        while stack:
            depth,node = stack.pop()
            # need to append kids to stack - (in the next iteration stack will 
            # pop node.right)
            if node.left:
                stack.append((depth+1,node.left))
            if node.right:
                stack.append((depth+1,node.right))
            maxDepth = max(maxDepth, depth)
        return maxDepth

    
