N=1000-int(input())
cnt=0
coin=[500,100,50,10,5,1]
for c in coin:
    cnt+=N//c
    N%=c
print(cnt)
    
    