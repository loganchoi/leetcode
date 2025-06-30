class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        #get maxDepth of nestedList

        def dfs(curList,depth):
            maxD = depth
            for elem in curList:
                if elem.isInteger() == False:
                    maxD = max(maxD,dfs(elem.getList(),depth+1))
            
            return maxD
        
        depth = dfs(nestedList,1)
        
        def res(curList,curLevel):
            total = 0
            for elem in curList:
                if elem.isInteger():
                    total += elem.getInteger() * curLevel
                else:
                    total += res(elem.getList(),curLevel-1)
            return total

        return res(nestedList,depth)
