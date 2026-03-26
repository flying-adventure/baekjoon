T = int(input())

for _ in range(T):
    a, b = input().split()

    if sorted(a) == sorted(b):
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")