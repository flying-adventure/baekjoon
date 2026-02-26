N=int(input())
paper=[]
for _ in range(N):
    paper.append(list(map(int,input().split())))
total=[[0]*100 for _ in range(100)]

for a,b in paper:
    for i in range(a,a+10):
        for j in range(b,b+10):
            total[i][j]=1
area=0
for i in range(100):
    for j in range(100):
        if total[i][j]==1:
            area+=1
print(area)