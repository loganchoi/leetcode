class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        res = []
        queue = deque()

        queue.append(root)
        while queue:
            nextLevel = deque()
            total = 0
            numNodes = len(queue)
            for curNode in queue:
                if curNode.left:
                    nextLevel.append(curNode.left)
                if curNode.right:
                    nextLevel.append(curNode.right)
                total = total + curNode.val
            res.append(total/numNodes)
            queue = nextLevel

        return res