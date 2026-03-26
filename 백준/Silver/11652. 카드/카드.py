import sys
input = sys.stdin.readline

N = int(input())
count = {}

for _ in range(N):
    num = int(input())
    count[num] = count.get(num, 0) + 1

print(sorted(count.items(), key=lambda x: (-x[1], x[0]))[0][0])