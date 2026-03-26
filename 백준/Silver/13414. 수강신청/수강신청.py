import sys
input = sys.stdin.readline

K, L = map(int, input().split())
d = {}

for i in range(L):
    student = input().strip()
    d[student] = i

result = sorted(d.items(), key=lambda x: x[1])

for student, _ in result[:K]:
    print(student)