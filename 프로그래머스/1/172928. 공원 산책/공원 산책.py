def solution(park, routes):
    N=len(park) #세로
    M=len(park[0]) #가로
    dir_dict = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

    #시작점 찾기
    sx,sy=0,0
    for i in range(N):
        for j in range(M):
            if park[i][j]=='S':
                sx,sy=i,j
        
    for ops in routes:
        op,n=ops.split()
        n=int(n)
        dx,dy=dir_dict[op]
        nx,ny=sx,sy
        is_ok=True
        for _ in range(n):
            nx+=dx
            ny+=dy
            if not(0<=nx<N and 0<=ny<M) or park[nx][ny]=='X':
                is_ok=False
                break
        if is_ok:
            sx,sy=nx,ny
        
    return sx,sy  