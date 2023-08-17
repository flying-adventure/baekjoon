cha_sc = 100
sang_sc = 100
n = int(input())
for _ in range(n):
    cha, sang = map(int,input().split())
    if cha > sang:
        sang_sc -= cha
    elif cha < sang:
        cha_sc -=sang

print(cha_sc)
print(sang_sc)