import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
S=input().strip()

answer=0
count=0
i=0
while i<(M-2):
    if S[i:i+3]=='IOI':
        count+=1
        i+=2
        if count==N:
            answer+=1
            count-=1
    else:
        count=0
        i+=1
print(answer)    