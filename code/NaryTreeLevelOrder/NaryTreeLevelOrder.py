"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)

        while queue:
            curLevel = []
            newLevel = []
            for node in queue:
                if node:
                    curLevel.append(node.val)
                    for c in node.children:
                        newLevel.append(c)

            res.append(curLevel)
            queue = newLevel
        
        return res
