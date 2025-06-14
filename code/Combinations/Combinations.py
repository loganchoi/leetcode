class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def backtrack(curCombo,curIndex):
            if len(curCombo) == k:
                res.append(curCombo + [])

            else:
                for i in range(curIndex,n+1):
                    curCombo = curCombo + [i]
                    backtrack(curCombo,i+1)
                    curCombo.pop()

        
        backtrack([],1)
        return res