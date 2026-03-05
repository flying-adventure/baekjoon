import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
a=[[] for _ in range(N+1)]
for _ in range(M):
    x,y=map(int,input().split())
    a[x].append(y)
    a[y].append(x)

def bacon(start):
    distance=[-1]*(N+1)
    queue=deque([start])
    distance[start]=0
    
    while queue:
        curr=queue.popleft()
        for neighbor in a[curr]:
            if distance[neighbor]==-1:
                distance[neighbor]=distance[curr]+1
                queue.append(neighbor)
    return sum(d for d in distance if d>0)

result=[]
for x in range(1,N+1):
    result.append(bacon(x))
print(result.index(min(result))+1)