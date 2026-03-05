import sys

input=sys.stdin.readline
N,r,c=map(int,input().split())

ans=0
while N!=0:
    N-=1
    size=2**N
    if r<size and c<size: #1사분면
        pass
    elif r>=size and c<size: #3사분면
        ans+=size*size*2
        r-=size
        
    elif r<size and c>=size: #2사분면
        ans+=size*size*1
        c-=size
    elif r>=size and c>=size: #4사분면
        ans+=size*size*3
        r-=size
        c-=size
        
print(ans)

