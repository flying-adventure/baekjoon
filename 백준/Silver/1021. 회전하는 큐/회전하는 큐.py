import sys
from collections import deque

# n: 큐의 크기, m: 뽑아내려는 수의 개수
n, m = map(int, sys.stdin.readline().split())
# 뽑아내려는 수의 위치들
targets = list(map(int, sys.stdin.readline().split()))

# 1부터 n까지 들어있는 덱 생성
dq = deque(range(1, n + 1))
total_count = 0

for target in targets:
    while True:
        # 1. 원하는 숫자가 맨 앞에 있으면 바로 뽑기
        if dq[0] == target:
            dq.popleft()
            break
            
        else:
            # 2. 원하는 숫자의 현재 인덱스를 찾음
            target_idx = dq.index(target)
            
            # 3. 중간 지점을 기준으로 왼쪽/오른쪽 중 가까운 쪽 선택
            
            # 왼쪽으로 가는 게 더 가깝거나 같을 때
            if target_idx <= len(dq) // 2:
                dq.append(dq.popleft()) # 왼쪽으로 회전
                total_count += 1
            # 오른쪽으로 가는 게 더 가까울 때
            else:
                dq.appendleft(dq.pop()) # 오른쪽으로 회전
                total_count += 1

print(total_count)