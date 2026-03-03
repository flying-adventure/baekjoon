import heapq
import sys

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    
    if x != 0:
        # 튜플 (절댓값, 실제값) 순서
        heapq.heappush(heap, (abs(x), x))
    else:
        if not heap:
            print(0)
        else:
            # 실제값
            print(heapq.heappop(heap)[1])