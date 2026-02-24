M=int(input())
N = list(input().strip())
values = []
for _ in range(M):
    values.append(int(input()))
bu=["+","-","/","*"]
for idx,x in enumerate(N):
    if x not in bu:
        N[idx] = values[ord(x) - ord('A')]
ans=[]
for x in N:
    if x not in bu:
        ans.append(x)
    else:
        b=ans.pop()
        a=ans.pop()
        if x==bu[0]:
            ans.append(a+b)
        if x==bu[1]:
            ans.append(a-b)
        if x==bu[2]:
            ans.append(a/b)
        if x==bu[3]:
            ans.append(a*b)
print(f"{ans[0]:.2f}")