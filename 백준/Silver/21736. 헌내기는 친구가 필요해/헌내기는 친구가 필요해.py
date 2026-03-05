import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N,M=map(int,input().split())
#N세로 M가로
#o빈공간 x벽 i도연 p사람
startx,starty=0,0
campus=[]
for r in range(N):
    row = list(input().strip())
    campus.append(row)
    for c in range(M):
        if row[c] == 'I': 
            startx, starty = r, c
dirs=[(1,0),(-1,0),(0,1),(0,-1)]
peo=0
visited=[[False]*M for _ in range(N)]

def dfs(a,b):
    global peo
    visited[a][b]=True
    if campus[a][b]=='P':
        peo+=1
    for x,y in dirs:
        nx,ny=a+x,b+y
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            if campus[nx][ny]!='X':
                dfs(nx,ny)
            
dfs(startx,starty)
print(peo if peo>0 else 'TT')