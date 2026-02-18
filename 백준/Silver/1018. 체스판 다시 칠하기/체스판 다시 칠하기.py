N,M=map(int,input().split())
board=[]
for _ in range(N):
    board.append(input().strip())
ans=64
for i in range(N-7):
    for j in range(M-7):
        count=0
        for r in range(8):
            for c in range(8):
                if (r+c)%2==0:
                    expected='W'
                    if board[i+r][j+c]!=expected:
                        count+=1
                else:
                    expected='B'
                    if board[i+r][j+c]!=expected:
                        count+=1
        ans=min(ans,count,64-count)
print(ans)
                
            
        
        
        