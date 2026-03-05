import sys
from collections import Counter
input=sys.stdin.readline

N,M,B=map(int,input().split())
#2차원말고 1차원으로 쭉 풀어서 받기
height=[]
for _ in range(N):
    height.extend(map(int,input().split()))
height_cnt=Counter(height)
min_time=float('inf')
best_height=0
low,high=min(height_cnt),max(height_cnt)

for target in range(low,high+1):
    removed,added=0,0
    for h, count in height_cnt.items():
        if h>target:
            removed+=(h-target)*count
        else:
            added+=(target-h)*count
    if removed + B>=added:
        time=removed*2+added
        if time<=min_time:
            min_time=time
            best_height=target
            
print(min_time,best_height)
