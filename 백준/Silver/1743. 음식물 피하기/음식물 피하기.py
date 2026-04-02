import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
grid = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    grid[r-1][c-1] = 1

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

max_size = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]:
            count = 1
            queue = deque([(i, j)])
            visited[i][j] = True
            
            while queue:
                curr_r, curr_c = queue.popleft()
                
                for dr, dc in dir:
                    nr, nc = curr_r + dr, curr_c + dc
                    
                    if 0 <= nr < n and 0 <= nc < m:
                        if grid[nr][nc] == 1 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
                            count += 1
            
            max_size = max(max_size, count)

print(max_size)