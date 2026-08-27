# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # path = []

        # def pathSums(root, targetSum, path):

        #     if not root:
                
        #         return False

        #     path.append(root.val)
        #     print(f'Current path {path}')

        #     if not root.right and not root.left:

        #         print(f"Leaf node reached {root.val}")
                
        #         if sum(path) == targetSum:
        #             return True
                
        #         else:
        #             print(f'Backtracking... removing {root.val}')
        #             path.pop()
        #             return False

        #     if pathSums(root.left, targetSum, path):
                
        #         return True

        #     if pathSums(root.right, targetSum, path):

        #         return True
            
        #     path.pop()
        #     return False

        # return pathSums(root, targetSum, path)

        def dfssum(node, curSum):

            if not node:
                return False

            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum
            
            return dfssum(node.left, curSum) or dfssum(node.right, curSum)

        return dfssum(root, 0)
