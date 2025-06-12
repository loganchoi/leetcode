# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []

        def dfs(node,total,curPath):
            if node == None:
                return
            if not node.left and not node.right:
                total = total +node.val
                curPath = curPath + [node.val]
                if targetSum == total:
                    print(curPath)
                    res.append(curPath)
                    
            dfs(node.left, total+node.val,curPath + [node.val])
            dfs(node.right,total+node.val,curPath + [node.val])

        dfs(root,0,[])

        return res