import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
dist=[[0]*M for _ in range(N)]
dirs=[(1,0),(-1,0),(0,1),(0,-1)]
cnt=0
mx_area=0
q=deque()

for i in range(N):
    for j in range(M):
        if board[i][j]==1 and dist[i][j]==0:
            cnt+=1
            q.append((i,j))
            dist[i][j]=1
            area=1
            while q:
                x,y=q.popleft()
                for dx,dy in dirs:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<N and 0<=ny<M and board[nx][ny]==1 and dist[nx][ny]==0:
                        dist[nx][ny]=1
                        q.append((nx,ny))
                        area+=1
                mx_area=max(mx_area,area)            
            
print(cnt)
print(mx_area)
