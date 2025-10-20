class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        for r in range(0,len(rooms)):
            for c in range(0,len(rooms[0])):
                if rooms[r][c] == 0:
                    queue.append((r,c,0))
        def bfs(row,col):
            visited = set()
            dirs = [(0,-1),(0,1),(1,0),(-1,0)]
            queue = deque()
            queue.append((row,col,0))
            while queue:
                curR, curC, dist = queue.popleft()
                for d in dirs:
                    nextR = curR + d[0]
                    nextC = curC + d[1]
                    if (0<= nextR < len(rooms) and 0 <= nextC < len(rooms[0]) 
                        and rooms[nextR][nextC] != -1 
                        and rooms[nextR][nextC] != 0 
                        and (nextR,nextC) not in visited):
                        nextDist = dist + 1
                        if nextDist <= rooms[nextR][nextC]:
                            rooms[nextR][nextC] = nextDist
                            queue.append((nextR,nextC,nextDist))
                        visited.add((nextR,nextC))

        for r in range(0,len(rooms)):
            for c in range(0,len(rooms[0])):
                if rooms[r][c] == 0:
                    queue.append((r,c,0))
