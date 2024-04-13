# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(node):
            if not node:
                return 0
            
            left_excess = dfs(node.left) if node.left else 0
            right_excess = dfs(node.right) if node.right else 0

            total_excess = node.val + left_excess + right_excess - 1

            self.moves += abs(total_excess)
    
            return total_excess

        
        dfs(root)

        return self.moves


        