# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        heap = []

        queue = [root]
        level = 1
        while queue:
            curLevel = queue
            nextLevel = []
            curTotal = 0

            for node in curLevel:
                curTotal += node.val
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            
            heapq.heappush(heap, (curTotal,level))
            level += 1
            queue = nextLevel
        
        return heap[0][1]
