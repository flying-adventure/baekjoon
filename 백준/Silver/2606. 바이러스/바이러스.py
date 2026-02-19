N=int(input())
M=int(input())
#전체탐색dfs재귀
#빈 리스트 선언
graph=[[] for _ in range(N+1)]
#인접노드입력받기
for _ in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
#방문하기
visited=[False]*(N+1)
def dfs(x):
    visited[x]=True
    for df in graph[x]:
        if not visited[df]:
            dfs(df)
dfs(1)
print(sum(visited)-1)