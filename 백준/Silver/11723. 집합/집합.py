import sys
input = sys.stdin.readline

m = int(input())
s = 0  # 비트마스크로 집합 표현

for _ in range(m):
    cmd = input().split()
    op = cmd[0]

    if op == "add":
        x = int(cmd[1])
        s |= (1 << x)

    elif op == "remove":
        x = int(cmd[1])
        s &= ~(1 << x)

    elif op == "check":
        x = int(cmd[1])
        print(1 if (s & (1 << x)) else 0)

    elif op == "toggle":
        x = int(cmd[1])
        s ^= (1 << x)

    elif op == "all":
        s = (1 << 21) - 2  # 1~20 비트만 1로 (0번 비트 제외)

    elif op == "empty":
        s = 0
