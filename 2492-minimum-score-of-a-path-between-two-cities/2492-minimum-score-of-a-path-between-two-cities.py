from collections import deque
from typing import List
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True

        ans = float('inf')

        while q:
            city = q.popleft()

            for nei, dist in graph[city]:
                ans = min(ans, dist)

                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)

        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna