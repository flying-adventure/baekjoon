# A_5분 B_1분 C_10초
Time = int(input())
    
A=300
B=60
C=10
a=0
b=0
c=0

while True:
    if Time % 10 != 0:
        print(-1)
        break
    if Time >= A:
        a+=1
        Time-=A
    elif Time >= B:
        b+=1
        Time-=B
    elif Time >= C:
        c+=1
        Time-=C
    if Time == 0:
        print(a,b,c)
        break
        
        