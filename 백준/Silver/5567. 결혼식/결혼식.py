import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

distances = [-1] * (n + 1)
distances[1] = 0
queue = deque([1])

while queue:
    curr = queue.popleft()
    
    for neighbor in adj[curr]:
        if distances[neighbor] == -1:
            distances[neighbor] = distances[curr] + 1
            queue.append(neighbor)

invite_count = 0
for i in range(2, n + 1):
    if 0 < distances[i] <= 2:
        invite_count += 1

print(invite_count)