M,N=map(int,input().split())
M_h=set(input().strip() for _ in range(M))
S=[input().strip() for _ in range(N)]
ans=0
for i in S:
    if i in M_h:
        ans+=1
print(ans)
