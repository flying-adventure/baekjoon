N=int(input())
num=[]
for _ in range(N):
    pri=int(input())
    if pri == 0:
        num.pop()
    else:
        num.append(pri)
print(sum(num))