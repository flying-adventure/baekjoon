import sys
input=sys.stdin.readline
N,M=map(int,input().split())
nohear=set()
for _ in range(N):
    nohear.add(input().strip())
ans=[]
for _ in range(M):
    name=input().strip()
    if name in nohear:
        ans.append(name)
ans.sort()
print(len(ans))
for i in ans:
    print(i)
