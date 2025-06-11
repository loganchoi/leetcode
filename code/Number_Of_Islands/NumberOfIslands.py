class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Method 1: BFS Traversal 
        #Data Structure: 2D Matrix
        #Time Complexity: ()

        #Step 1: Traverse through the matrix, and find a "1"
        #Step 2: After finding the "1", run through bfs to see what it is connected
        #Step 3: After finding all of them, increment the total number of islands
        #BE MINDFUL OF THE FOLLOWING:
        #Being out of bounds, and not revisiting the same node

        rows = len(grid)
        cols = len(grid[0])
        seenCoords = set()


        def islandBFS(r,c):
            directions = [[0,-1],[-1,0],[0,1],[1,0]]

            queue = deque()
            queue.append((r,c))

            while queue:
                curRow, curCol = queue.popleft()
                seenCoords.add((curRow,curCol))
                for d in directions:
                    nextRow = curRow + d[0]
                    nextCol = curCol + d[1]
                    if (0 <= nextRow < rows and 0<= nextCol < cols and (nextRow, nextCol) not in seenCoords
                        and grid[nextRow][nextCol]=="1"):
                        queue.append((nextRow,nextCol))
                        seenCoords.add((nextRow,nextCol))
            return

        total = 0
        for x in range(0,rows):
            for y in range(0,cols):
                if grid[x][y] == "1" and (x,y) not in seenCoords:
                    islandBFS(x,y)
                    total = total + 1

        return total