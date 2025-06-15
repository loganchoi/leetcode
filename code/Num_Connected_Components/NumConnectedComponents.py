class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = []

        for i in range(0,n):
            graph.append([])
        
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        visited = set()

        def bfs(node):
            queue = deque()
            queue.append(node)

            while queue:
                curNode = queue.pop()
                visited.add(curNode)
                for nextNode in graph[curNode]:
                    if nextNode not in visited:
                        queue.append(nextNode)

        total = 0
        for i in range(0,n):
            if i not in visited:
                bfs(i)
                total = total+1
        
        return total