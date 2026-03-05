def solution(dirs):
    visited_paths = set()
    x, y = 5, 5
    move = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    for d in dirs:
        dx, dy = move[d]
        nx, ny = x + dx, y + dy
        
        if 0 <= nx <= 10 and 0 <= ny <= 10:
            # "A -> B"와 "B -> A"를 같은 길로 취급-> 정렬해서 저장
            path = tuple(sorted([(x, y), (nx, ny)]))
            visited_paths.add(path)
            x, y = nx, ny
            
    return len(visited_paths)