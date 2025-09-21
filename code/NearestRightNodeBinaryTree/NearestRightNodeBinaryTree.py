# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        
        queue = [root]

        while queue:
            currLevel = queue
            nextLevel = []
            for i in range(0,len(currLevel)):
                if currLevel[i] == u:
                    if i != len(currLevel) - 1:
                        return currLevel[i+1]
                    else:
                        return None

                if currLevel[i].left:
                    nextLevel.append(currLevel[i].left)
                if currLevel[i].right:
                    nextLevel.append(currLevel[i].right)
            
            queue = nextLevel