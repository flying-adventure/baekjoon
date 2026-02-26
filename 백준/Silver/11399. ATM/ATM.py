N=int(input())
peo=list(map(int,input().split()))
peo.sort()
ans=0
k=0
for i in peo:
    k+=i
    ans+=k
print(ans)
