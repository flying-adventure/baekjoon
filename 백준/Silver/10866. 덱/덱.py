import sys
from collections import deque

input = sys.stdin.read().splitlines()
n = int(input[0])
dq = deque()
results = []

for i in range(1, n + 1):
    command = input[i].split()
    
    if command[0] == 'push_front':
        dq.appendleft(command[1])
    elif command[0] == 'push_back':
        dq.append(command[1])
    elif command[0] == 'pop_front':
        results.append(dq.popleft() if dq else "-1")
    elif command[0] == 'pop_back':
        results.append(dq.pop() if dq else "-1")
    elif command[0] == 'size':
        results.append(str(len(dq)))
    elif command[0] == 'empty':
        results.append("0" if dq else "1")
    elif command[0] == 'front':
        results.append(dq[0] if dq else "-1")
    elif command[0] == 'back':
        results.append(dq[-1] if dq else "-1")
print("\n".join(results))