import sys
input = sys.stdin.readline

N = int(input().strip())
light = list(map(int, input().split()))
S = int(input().strip())

for _ in range(S):
    a, b = map(int, input().split())

    if a == 1:  # 남학생
        for i in range(b - 1, N, b):
            light[i] ^= 1

    else:  # 여학생
        idx = b - 1
        l = r = idx
        while l - 1 >= 0 and r + 1 < N and light[l - 1] == light[r + 1]:
            l -= 1
            r += 1
        for i in range(l, r + 1):
            light[i] ^= 1

for i in range(0, N, 20):
    print(*light[i:i+20])