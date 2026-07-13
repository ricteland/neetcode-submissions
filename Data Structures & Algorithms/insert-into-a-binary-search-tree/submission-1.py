# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # if not root:

        #     return TreeNode(val = val)

        # if val > root.val:

        #     root.right = self.insertIntoBST(root.right, val)

        # elif val < root.val:

        #     root.left = self.insertIntoBST(root.left, val)

        # return root

        if not root:

            return TreeNode(val)

        pointer = root
        while True:

            if val > pointer.val:

                if not pointer.right:

                    pointer.right = TreeNode(val)
                    return root

                pointer = pointer.right

            elif val < pointer.val:

                if not pointer.left:

                    pointer.left = TreeNode(val)
                    return root

                pointer = pointer.left



        
