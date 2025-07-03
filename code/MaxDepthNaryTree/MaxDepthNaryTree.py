class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0

        def dfs(node,depth):
            if node == None:
                return depth
            if not node.children:
                return depth
            maxD = depth
            for c in node.children:
                maxD = max(maxD,dfs(c,depth+1))
            
            return maxD

        return dfs(root,1)