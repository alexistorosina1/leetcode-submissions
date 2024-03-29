# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        if root.left and root.right:
            left_subtree = self.minDepth(root.left)
            right_subtree = self.minDepth(root.right)
            return min(left_subtree, right_subtree) + 1

        if root.left:
            return self.minDepth(root.left) + 1
        if root.right:
            return self.minDepth(root.right) + 1

        return 1

