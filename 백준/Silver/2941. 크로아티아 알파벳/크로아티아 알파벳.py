cro=['c=','c-','dz=','d-','lj','nj','s=','z=']
N=input().strip()
cnt=0
for s in cro:
        N=N.replace(s,'@')
print(len(N))
        