from collections import Counter
N=int(input())
li=[]
for _ in range(N):
    a,b=input().split()
    li.append((a,b))
cnt=Counter(a for a,_ in li)
left=[]
for x,y in cnt.items():
    if y%2!=0:
        left.append(x)
left.sort(reverse=True)
for name in left:
    print(name)
