N=int(input())
stack=[]
ans=[]
current=1
for _ in range(N):
    target=int(input())
    while current <= target:
        stack.append(current)
        current+=1
        ans.append("+")
    if stack[-1]==target:
        stack.pop()
        ans.append("-")
    else:
        print("NO")
        exit()
for op in ans:
    print(op)