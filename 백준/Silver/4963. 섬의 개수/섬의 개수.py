import sys
from collections import deque

input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
        
    grid = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    
    count = 0
    

    dir = [(1,0), (-1,0), (0,1), (0,-1), (-1,-1), (1,1), (-1,1), (1,-1)]
    
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                count += 1
                queue = deque([(i, j)])
                visited[i][j] = True
                
                while queue:
                    curr_h, curr_w = queue.popleft()
                    
                    for dh, dw in dir:
                        nh, nw = curr_h + dh, curr_w + dw
                        
                        if 0 <= nh < h and 0 <= nw < w:
                            if grid[nh][nw] == 1 and not visited[nh][nw]:
                                visited[nh][nw] = True
                                queue.append((nh, nw))
                                
    print(count)