import sys
input=sys.stdin.readline
N=int(input())
mem=[]
for _ in range(N):
    n,k,e,m=input().split()
    mem.append((n,int(k),int(e),int(m)))
mem.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for x in mem:
    print(x[0])
    