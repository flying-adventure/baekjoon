import sys
input=sys.stdin.readline
K,N=map(int,input().split())
lan=[int(input()) for _ in range(K)]

#K개의 개수 랜선을 잘라 동일한 길이의 N개 랜선을 만들자
start,end=1,max(lan)
result=0

while start<=end:
    mid=(start+end)//2
    total_pieces = 0
    for x in lan:
        total_pieces += x//mid
    if total_pieces>=N:
        result=mid
        start=mid+1
    else:
        end=mid-1
print(result)

    