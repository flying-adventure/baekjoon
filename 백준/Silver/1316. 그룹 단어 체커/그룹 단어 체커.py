N=int(input())
ans=0

for _ in range(N):
    ch=True
    alpha=set()
    word=list(input().strip())
    prev=''
    for i in word:
        if i !=prev:
            if i in alpha:
                ch=False
                break
            alpha.add(i)
        prev=i
    if ch:ans+=1      
print(ans)
            
            
        