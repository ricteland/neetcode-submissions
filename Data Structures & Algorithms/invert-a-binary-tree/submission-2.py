# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        # If empty return root
        if not root:
            return root

        # If leaf return leaf
        if not root.right and not root.left:
            return root

        #Swap child
        root.right, root.left = root.left, root.right

        #First lhs, then rhs
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

