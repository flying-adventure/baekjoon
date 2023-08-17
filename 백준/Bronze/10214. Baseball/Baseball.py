T = int(input())

for _ in range(T):
    y_sc=0
    k_sc=0
    for _ in range(9):
        Y, K = map(int,input().split())
        y_sc += Y
        k_sc += K
    if y_sc > k_sc:
        print("Yonsei")
    elif y_sc < k_sc:
        print("Korea")
    else:
        print("Draw")