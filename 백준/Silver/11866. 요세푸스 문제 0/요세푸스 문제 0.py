from collections import deque
N,K=map(int,input().split())
ans=[]
queue=deque()
for i in range(1,N+1):
    queue.append(i)
while queue:
    current=1
    while current!=K:
        queue.append(queue.popleft())
        current+=1
    if current==K:
        ans.append(queue.popleft())
        current=1
print("<" + ", ".join(map(str, ans)) + ">")

