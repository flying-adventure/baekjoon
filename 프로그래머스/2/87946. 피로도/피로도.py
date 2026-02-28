#던전이 8개 밖에 안됨 -> 완전탐색
def dfs(k,cnt,dungeons,visited):
    global ans
    ans=max(ans,cnt)
    
    for i in range(len(dungeons)):
        a,b=dungeons[i]
        if not visited[i]and k>=a:
            visited[i]=True
            dfs(k-b,cnt+1,dungeons,visited)
            visited[i]=False
    
def solution(k, dungeons):
    global ans
    ans=0
    cnt=0
    visited=[False]*len(dungeons)
    dfs(k,0,dungeons,visited)
    return ans
    