class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #Get boundaries of the board
        rowBound, colBound = len(board), len(board[0])

        #In the backtrack function, we should build the string accordingly
        #Based off the input and moves only up,down,left,right. 
        #Be mindful of going past any boundaries
        #Have a list or set of coordinates to ensure you do not revisit a square
        def backtrack(r,c,seen,curStr):
            if curStr == word:
                return True
            if curStr not in word:
                return False
            else:
                seen.add((r,c))
                directions = [[-1,0],[1,0],[0,-1],[0,1]]
                for d in directions:
                    row = r + d[0]
                    col = c + d[1]
                    if row >= 0 and col >= 0 and row < rowBound and col < colBound and (row,col) not in seen:
                        curStr = curStr + board[row][col]
                        if backtrack(row,col,seen,curStr):
                            return True
                        curStr = curStr[:-1]
                seen.remove((r,c))
                return False

        #Find the first letter in the grid then pass it to backtrack 
        for x in range(0,rowBound):
            visited = set()
            for y in range(0,colBound):
                if board[x][y] == word[0]:
                    if backtrack(x,y,visited,word[0]):
                        return True

        #We will assume that it will not be there
        return False 









