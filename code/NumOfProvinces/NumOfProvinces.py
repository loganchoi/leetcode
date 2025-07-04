class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                queue = deque([i])
                while queue:
                    city = queue.popleft()
                    for neighbor in range(n):
                        if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                provinces += 1

        return provinces