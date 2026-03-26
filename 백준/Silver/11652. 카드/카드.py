import sys
input = sys.stdin.readline

def my_key(x):
    return (-x[1], x[0])

N = int(input())
count = {}

for _ in range(N):
    num = int(input())
    count[num] = count.get(num, 0) + 1

result = sorted(count.items(), key=my_key)
print(result[0][0])