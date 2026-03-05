import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
#n세로 m가로
board=[]
sx,sy=0,0
for k in range(n):
    board.append(list(map(int,input().split())))
    for j in range(m):
        if board[k][j]==2:
            sx,sy=k,j
            
visited=[[-1]*m for _ in range(n)]
visited[sx][sy]=0
dirs=[(0,1),(0,-1),(1,0),(-1,0)]
q=deque([(sx,sy)])

while q:
    x,y=q.popleft()
    for dx,dy in dirs:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1:
            if board[nx][ny]==1:
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))
            elif board[nx][ny]==0:
                visited[nx][ny]=0
for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            print(0,end=' ')
        else:
            print(visited[i][j],end=' ')
    print()
   
