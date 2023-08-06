now = list(map(int, input().split()))
now[1]+= int(input())
while now[1]>=60 or now[0]>23:
    if now[1]>=60:
        now[0]+=1
        now[1]-=60
    if now[0]>23:
        now[0]=0
print(now[0],now[1])
