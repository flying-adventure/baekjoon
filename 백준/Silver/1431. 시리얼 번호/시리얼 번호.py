N=int(input())
g=[]
def digit_sum(x:str)->int:
    return sum(int(c) for c in x if c.isdigit())
for _ in range(N):
    g.append(input().strip())
g.sort(key=lambda x: (len(x),digit_sum(x),x))
for i in g:
    print(i)

