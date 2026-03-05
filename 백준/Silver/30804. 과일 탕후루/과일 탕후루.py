import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
fruits = list(map(int, input().split()))

left = 0
max_fruits = 0
count_dict = Counter()
kind_count = 0

for right in range(N):
    # 오른쪽 과일 추가
    if count_dict[fruits[right]] == 0:
        kind_count += 1
    count_dict[fruits[right]] += 1 
    # 과일 종류가 2개를 초과하면, 왼쪽을 당겨서 종류를 줄임
    while kind_count > 2:
        count_dict[fruits[left]] -= 1
        if count_dict[fruits[left]] == 0:
            kind_count -= 1
        left += 1
    
    # 현재 구간의 길이(right - left + 1) 중 최댓값 갱신
    max_fruits = max(max_fruits, right - left + 1)

print(max_fruits)