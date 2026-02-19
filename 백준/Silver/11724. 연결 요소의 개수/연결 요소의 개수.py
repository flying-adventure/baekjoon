import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]


#인접 리스트 만들기
for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
#방문 리스트 만들기
visited=[False]*(N+1)

def dfs(x):
    visited[x]=True
    for nx in graph[x]:
        if not visited[nx]:
            dfs(nx)
            
count=0
for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        count+=1
print(count)
        