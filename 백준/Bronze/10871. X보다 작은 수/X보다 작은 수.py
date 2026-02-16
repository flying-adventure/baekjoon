n,x=map(int,input().split())
k=list(map(int,input().split()))
print(*[h for h in k if h<x])
