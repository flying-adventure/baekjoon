import sys
input=sys.stdin.readline
N,K=map(int,input().split())
coins=[]
for _ in range(N):
    coins.append(int(input().strip()))
coins.sort(reverse=True)
cnt=0
for c in coins:
    cnt+=K//c
    K%=c
print(cnt)
    