H,W=map(int,input().split())
block=list(map(int,input().split()))
ans=0

for i in range(1,W-1):
    left_max=max(block[:i+1])
    right_max=max(block[i:])
    ans+= min(left_max,right_max)-block[i]

print(ans)
    