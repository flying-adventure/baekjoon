import sys
input=sys.stdin.readline
#누적합=끝지점까지의합-시작부터의합
N,M=map(int,input().split())
su=list(map(int,input().split()))
sum_list=[0]
k=0
for i in range(N):
    k+=su[i]
    sum_list.append(k)
    
for _ in range(M):
    i,j=map(int,input().split())
    print(sum_list[j]-sum_list[i-1])
    