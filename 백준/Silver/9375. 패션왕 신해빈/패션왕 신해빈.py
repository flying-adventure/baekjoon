from collections import Counter
n=int(input())
for _ in range(n):
    clo=[]
    m=int(input())
    for _ in range(m):
        a,b=input().split()
        clo.append(b)
    cnt=Counter(clo)
    result=1
    for i in cnt.values():
        result*=(i+1)
    print(result-1)
        
        