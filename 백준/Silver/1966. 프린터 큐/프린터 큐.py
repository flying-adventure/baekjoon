from collections import deque
#테스트케이스 수
N=int(input())
for _ in range(N):
    count=0
    num, target = map(int,(input().split()))
    #중요도 입력
    priorities=list(map(int,input().split()))
    queue=deque()
    #중요도,인덱스 튜플 저장
    for i in range(num):
        queue.append((priorities[i],i))
    while queue:
        priority, idx=queue.popleft()
        if any(priority<other[0] for other in queue):
            queue.append((priority,idx))
        else:
            count+=1
            if idx==target:
                print(count)
                break