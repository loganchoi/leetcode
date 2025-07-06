class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        res = []

        for r in range(0,len(matrix)):
            for c in range(0,len(matrix)):
                if len(res) == k:
                    if -matrix[r][c] > res[0]:
                        heapq.heappop(res)
                        heapq.heappush(res,-matrix[r][c])
                
                else:
                    heapq.heappush(res,-matrix[r][c])

        return -res[0]