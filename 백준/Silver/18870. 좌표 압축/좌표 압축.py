import sys
input=sys.stdin.readline
N=int(input())
arr=list(map(int,input().split()))
sorted_arr=sorted(list(set(arr)))
dic={val:i for i,val in enumerate(sorted_arr)}
for x in arr:
    print(dic[x],end=' ')