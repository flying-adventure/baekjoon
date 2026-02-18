import sys
input = sys.stdin.readline

N=int(input())
if N==0:
    print(0)
else:
    k = int(N * 0.15 + 0.5)
    score=[]
    for _ in range(N):
        score.append(int(input()))
    score.sort()
    result=score[k:N-k]
    avg=int(sum(result)/len(result)+0.5)
    print(avg)