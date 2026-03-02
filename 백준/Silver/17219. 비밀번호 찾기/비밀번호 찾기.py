import sys
input=sys.stdin.readline

N,M=map(int,input().split())

k={}
for _ in range(N):
    site,password=input().split()
    k[site]=password
for _ in range(M):
    print(k[input().strip()])
    
