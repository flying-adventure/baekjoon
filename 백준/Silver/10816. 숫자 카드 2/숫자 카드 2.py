from collections import Counter
N=int(input())
cards=[]

cards=map(int,input().split())
cnt=Counter(cards)
M=int(input())

targets=list(map(int,input().split()))
for i in targets:
    print(cnt[i],end=" ")

    