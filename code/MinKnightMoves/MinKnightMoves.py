class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dirs = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]

        queue = deque()

        queue.append((0,0,0))
        seen = set()
        seen.add((0,0))
        while queue:
            curR, curC, curMoves = queue.popleft()
            if curR == x and curC == y:
                return curMoves
            for d in dirs:
                nextR = curR + d[0] 
                nextC = curC + d[1]
                if (nextR,nextC) not in seen:
                    queue.append((nextR,nextC, curMoves+1))
                    seen.add((nextR,nextC))
                