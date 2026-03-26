T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))
    arr.sort()

    mid = arr[1:4]

    if mid[2] - mid[0] >= 4:
        print("KIN")
    else:
        print(sum(mid))