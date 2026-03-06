from collections import deque
def solution(maps):
    
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    N=len(maps[0]) #가로
    M=len(maps) #세로
    q=deque([(0,0)])
    
    while q:
        x,y=q.popleft()
        for dx,dy in dirs:
            nx,ny=x+dx,y+dy
            if 0<=nx<M and 0<=ny<N and maps[nx][ny]==1:
                maps[nx][ny]=maps[x][y]+1
                q.append((nx,ny))
        
        
    path=maps[M-1][N-1]
    
    
    return path if path>1 else -1
        
    