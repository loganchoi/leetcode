class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newHead = TreeNode(val,root,None)
            return newHead

        def dfs(curNode,parent,curDepth,left):
            if curNode == None and curDepth == depth:
                newNode = TreeNode(val,None,None)
                if left: 
                    parent.left = newNode
                else:
                    parent.right = newNode
            if curNode == None and curDepth != depth:
                return
            if curDepth == depth:
                newNode = TreeNode(val,None,None)
                if left:
                    newNode.left = curNode
                    parent.left = newNode
                else:
                    newNode.right = curNode
                    parent.right = newNode
                return
            
            dfs(curNode.left,curNode,curDepth+1,True)
            dfs(curNode.right,curNode,curDepth+1,False)



        dfs(root,None,1,False)
        return root