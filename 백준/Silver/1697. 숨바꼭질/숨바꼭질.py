import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100000

dist = [-1] * (MAX + 1)
q = deque([N])
dist[N] = 0

while q:
    cur = q.popleft()

    if cur == K:
        print(dist[cur])
        break

    for nxt in (cur - 1, cur + 1, cur * 2):
        if 0 <= nxt <= MAX and dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)
