N=int(input())
peo=sorted(map(int,input().split()))
ans=0
cur=0
for i in range(N):
    cur+=peo[i]
    ans+=cur
    
print(ans)