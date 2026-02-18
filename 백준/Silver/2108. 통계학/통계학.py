from collections import Counter
import sys
input=sys.stdin.readline

num = int(input())
nums = [int(input()) for _ in range(num)]

# 산술평균
avg = sum(nums) / num
if avg >= 0:
    print(int(avg + 0.5))
else:
    print(int(avg - 0.5))

# 중앙값
nums.sort()
print(nums[num//2])

# 최빈값
counter = Counter(nums)
max_freq = max(counter.values())
vals = [val for val, freq in counter.items() if freq == max_freq]
vals.sort()

if len(vals) > 1:
    print(vals[1])
else:
    print(vals[0])

# 범위
print(nums[-1] - nums[0])
