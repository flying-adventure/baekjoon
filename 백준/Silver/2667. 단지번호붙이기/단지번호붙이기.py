from collections import deque
#덩어리 개수 세기 -> dfs아닌감
N=int(input())
board=[list(map(int,input().strip())) for _ in range(N)]
dirs=[(1,0),(-1,0),(0,1),(0,-1)]
dist=[[0]*N for _ in range(N)]

def bfs(sx,sy):
    q=deque([(sx,sy)])
    dist[sx][sy]=1
    cnt=1
    while q:
        x,y=q.popleft()
        for dx,dy in dirs:
            nx,ny=x+dx,y+dy
            if 0<=nx<N and 0<=ny<N:
                if dist[nx][ny]==0 and board[nx][ny]==1:
                    dist[nx][ny]=1
                    q.append((nx,ny))
                    cnt+=1
    return cnt
sizes=[]
for i in range(N):
    for j in range(N):
        if board[i][j]==1 and dist[i][j]==0:
            sizes.append(bfs(i,j))

sizes.sort()
print(len(sizes))
for i in sizes:
    print(i)
    

