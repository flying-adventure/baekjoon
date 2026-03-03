import sys
from collections import deque
input = sys.stdin.readline

N,M,V=map(int,input().split())
board=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    board[a].append(b)
    board[b].append(a)
#작은 번호부터 방문하기 위한 정렬
for i in range(1,N+1):
    board[i].sort()

dfs_visited=[False]*(N+1)
def dfs(v,dfs_visited):
    dfs_visited[v]=True
    print(v,end=' ')
    for neighbor in board[v]:
        if not dfs_visited[neighbor]:
            dfs(neighbor,dfs_visited)
def bfs(v):
    queue=deque([v])
    bfs_visited=[False]*(N+1)
    bfs_visited[v]=True
    while queue:
        curr=queue.popleft()
        print(curr,end=' ')
        for neighbor in board[curr]:
            if not bfs_visited[neighbor]:
                bfs_visited[neighbor]=True
                queue.append(neighbor)
dfs(V,dfs_visited)
print()
bfs(V)
    
    