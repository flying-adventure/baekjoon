def solution(park, routes):
    # 1. 초기 설정
    H = len(park)
    W = len(park[0])
    
    # 시작 위치 찾기
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                r, c = i, j
                break
                
    # 방향 매핑
    dirs = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
    
    # 2. 명령 수행
    for route in routes:
        op, n = route.split()
        n = int(n)
        dr, dc = dirs[op]
        
        nr, nc = r, c
        can_move = True
        
        # 3. 한 칸씩 이동하며 검증 (n번 반복)
        for _ in range(n):
            nr += dr
            nc += dc
            
            # 공원을 벗어나거나 장애물을 만나는지 체크
            if not (0 <= nr < H and 0 <= nc < W) or park[nr][nc] == 'X':
                can_move = False
                break
        
        # 검증을 통과했을 때만 실제 좌표 업데이트
        if can_move:
            r, c = nr, nc
            
    return [r, c]