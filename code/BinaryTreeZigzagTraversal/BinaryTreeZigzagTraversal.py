class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)

        res = []
        left = True
        while queue:
            nextLevel = deque()
            levelVals = []
            for curNode in queue:
                if curNode.left:
                    nextLevel.append(curNode.left)
                if curNode.right:
                    nextLevel.append(curNode.right)
                levelVals.append(curNode.val)
           
            if not left:
                res.append(levelVals[::-1])
            else:
                res.append(levelVals)
            
            left = not left
            queue = nextLevel
        return res