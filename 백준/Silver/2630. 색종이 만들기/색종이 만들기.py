import sys
input=sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
white=0
blue=0
def dfs(r,c,n):
    #사각형이 모두 같은 숫잔지 확인 다르면 4등분한 재귀4개 반환
    global white,blue
    color=board[r][c] #현재 칸의 색
    for i in range(r,r+n):
        for j in range(c,c+n):
            if board[i][j]!=color:
                half=n//2
                dfs(r,c,half)
                dfs(r,c+half,half)
                dfs(r+half,c,half)
                dfs(r+half,c+half,half)
                return
    if color==0:
        white+=1
    else:
        blue+=1
dfs(0,0,N)
print(white)
print(blue)
