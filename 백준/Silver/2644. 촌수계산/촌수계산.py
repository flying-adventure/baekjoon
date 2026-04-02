import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
target_a, target_b = map(int, input().split())
m = int(input())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

distances = [-1] * (n + 1)
distances[target_a] = 0
queue = deque([target_a])

while queue:
    curr = queue.popleft()
    
    if curr == target_b:
        break
        
    for neighbor in adj[curr]:
        if distances[neighbor] == -1:
            distances[neighbor] = distances[curr] + 1
            queue.append(neighbor)

print(distances[target_b])