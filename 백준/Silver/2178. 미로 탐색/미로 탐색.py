import sys
from collections import deque
input=sys.stdin.readline

#미로 -> bfs, 방문여부+횟수 dist 리스트 필요, 큐
N,M=map(int,input().split())
board=[list(map(int,input().strip())) for _ in range(N)]

##시작칸 설정
dist=[[0]*M for _ in range(N)]
dist[0][0]=1 
q=deque([(0,0)])
dirs=[(1,0),(-1,0),(0,1),(0,-1)]

#순회: 큐에서 하나를 뺌, for문에 방향 고려하고 새로운 변수에 넣기, if board 범위, if 갈수있고and방문안한곳
#방문횟수 증가시키고 큐에 좌표 넣기
while q:
    x,y=q.popleft()
    for dx,dy in dirs:
        nx,ny=x+dx,y+dy
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny]==1 and dist[nx][ny] ==0:
                dist[nx][ny]=dist[x][y]+1
                q.append((nx,ny))
# 좌표 0부터 시작하는거 항상 고려하기               
print(dist[N-1][M-1])