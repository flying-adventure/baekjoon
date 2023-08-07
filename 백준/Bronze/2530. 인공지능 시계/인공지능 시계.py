now = list(map(int,input().split()))
now[2]+=int(input())

while now[0]>23 or now[1]>59 or now[2]>59:
    if now[0]>23:
        now[0]=0
    if now[1]>59:
        now[0]+=1
        now[1]-=60
    if now[2]>59:
        now[1]+=1
        now[2]-=60
print(now[0],now[1],now[2])