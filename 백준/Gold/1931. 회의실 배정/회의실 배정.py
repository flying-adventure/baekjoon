import sys
input=sys.stdin.readline
N=int(input())
team=[]
for _ in range(N):
    s,e=map(int,input().split())
    team.append((s,e))
team.sort(key=lambda x: (x[1],x[0]))
cnt=0
end_time=0
for s,e in team:
    if s>=end_time:
        cnt+=1
        end_time=e
print(cnt)
    