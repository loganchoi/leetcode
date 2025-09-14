# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sumCount = {}
        def dfs(curNode):
            if curNode == None:
                return 0
            else:
                nodeTotal = dfs(curNode.left) + dfs(curNode.right) + curNode.val
                if nodeTotal in sumCount.keys():
                    sumCount[nodeTotal] += 1
                else:
                    sumCount[nodeTotal] = 1
                return nodeTotal

        dfs(root)

        countMax = max(sumCount.values())

        res = []
        for nodeTotal, count in sumCount.items():
            if count == countMax:
                res.append(nodeTotal)
        
        return res