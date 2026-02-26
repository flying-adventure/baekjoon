import sys
input = sys.stdin.readline

N = int(input().strip())
board = [list(input().strip()) for _ in range(N)]

def check():
    best = 1
    # 가로 체크
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                if cnt > best: best = cnt
                cnt = 1
        if cnt > best: best = cnt

    # 세로 체크
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if board[i][j] == board[i-1][j]:
                cnt += 1
            else:
                if cnt > best: best = cnt
                cnt = 1
        if cnt > best: best = cnt

    return best

ans = check()  # 교환 안 해도 최댓값일 수 있음

for i in range(N):
    for j in range(N):
        # 오른쪽과 교환
        if j + 1 < N and board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            ans = max(ans, check())
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        # 아래와 교환
        if i + 1 < N and board[i][j] != board[i+1][j]:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            ans = max(ans, check())
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(ans)