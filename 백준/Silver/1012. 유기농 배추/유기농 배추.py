import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(i,j,M,N,board):
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    board[i][j]=0
    for dx,dy in dirs:
        nx,ny=i+dx,j+dy
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny]==1:
                dfs(nx,ny,M,N,board)
T=int(input())
for _ in range(T):
    M,N,K=map(int,input().split())
    board=[[0]*M for _ in range(N)]
    for _ in range(K):
        i,j=map(int,input().split())
        board[j][i]=1
    
    div=0
    #board를 막 바꿔도 되니까,, 굳이 visited 배열안만들어도 됨
    for i in range(N):
        for j in range(M):
            if board[i][j]==1:
                dfs(i,j,M,N,board)
                div+=1
    print(div)
    
    