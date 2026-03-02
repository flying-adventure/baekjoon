import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    zero = [1, 0]
    one = [0, 1]
    
    # 2부터 n까지 반복하며 피보나치 방식으로 더함
    if n >= 2:
        for i in range(2, n + 1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
            
    print(f"{zero[n]} {one[n]}")