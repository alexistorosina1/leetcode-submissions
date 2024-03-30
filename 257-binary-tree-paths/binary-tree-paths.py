# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def dfs(node, path):
            if not node:
                return
            # Add the current node's value to the path
            path += str(node.val)
            # If the current node is a leaf node, add the path to the list of paths
            if not node.left and not node.right:
                paths.append(path)
            else:
                # Recursively traverse the left and right subtrees
                dfs(node.left, path + "->")
                dfs(node.right, path + "->")
        
        # Start DFS traversal from the root with an empty path
        dfs(root, "")
        
        return paths