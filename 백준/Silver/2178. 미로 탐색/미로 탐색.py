import sys
from collections import deque
input=sys.stdin.readline

#미로 -> bfs, 방문여부+횟수 dist 리스트 필요, 큐
N,M=map(int,input().split())
board=[list(map(int,input().strip())) for _ in range(N)]

dist=[[0]*M for _ in range(N)]
dist[0][0]=1 
q=deque([(0,0)])
dirs=[(1,0),(-1,0),(0,1),(0,-1)]

while q:
    x,y=q.popleft()
    
    for dx,dy in dirs:
        nx,ny=x+dx,y+dy
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny]==1 and dist[nx][ny] ==0:
                dist[nx][ny]=dist[x][y]+1
                q.append((nx,ny))
print(dist[N-1][M-1])