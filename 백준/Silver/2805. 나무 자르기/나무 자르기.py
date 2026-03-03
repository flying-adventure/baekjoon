import sys
from collections import Counter

input = sys.stdin.readline
N, M = map(int, input().split())
trees = Counter(map(int, input().split())) # 나무 높이별 개수를 센다

start, end = 0, max(trees.keys())
result = 0

while start <= end:
    mid = (start + end) // 2
    
    # 중복된 나무를 묶어서 한꺼번에 계산
    total = sum((height - mid) * count for height, count in trees.items() if height > mid)
    
    if total >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)