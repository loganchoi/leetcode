# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.maxRes = 0

        def dfs(node, prevVal, streak):
            if node is None:
                self.maxRes = max(self.maxRes, streak)
                return
            else:
                self.maxRes = max(self.maxRes, streak)
                if node.val - 1 == prevVal:
                    streak = streak + 1
                else:
                    streak = 1
                dfs(node.left,node.val,streak)
                dfs(node.right,node.val,streak)
        
        dfs(root, -math.inf, 1)

        return self.maxRes