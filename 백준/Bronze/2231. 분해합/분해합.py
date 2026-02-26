n=int(input())
z=n-1
m=[]
while z!=0:
    k=list(map(int,str(z)))
    if z+sum(k)==n:
        m.append(z)
    z-=1
    
print(min(m) if m else 0)
    