#bfs
import sys
from collections import deque
input=sys.stdin.readline

#1=익은 토마토, 0은 익지 않은 토마토
N,M=map(int,input().split()) #N가로 M세로
board=[list(map(int,input().split())) for _ in range(M)]
q=deque()
dirs=[(1,0),(-1,0),(0,1),(0,-1)]

#처음부터 익어 있는 토마토를 큐에 전부 넣어놓고 시작
for i in range(M):
    for j in range(N):
        if board[i][j]==1:
            q.append((i,j))
#큐 돌리기
while q:
    x,y=q.popleft()
    for dx,dy in dirs:
        nx,ny=x+dx,y+dy
        if 0<=nx<M and 0<=ny<N and board[nx][ny]==0:
            board[nx][ny]=board[x][y]+1
            q.append((nx,ny))
            
#전체 중 가장 높은 일수 == 전체가 익은 최소일수
mx=0
for i in range(M):
    for j in range(N):
        if board[i][j]==0:
            print(-1)
            sys.exit(0)
        if mx<board[i][j]:
            mx=board[i][j]
print(mx-1)
