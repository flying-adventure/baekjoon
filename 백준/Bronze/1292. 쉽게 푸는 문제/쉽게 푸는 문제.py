N,M=map(int,input().split())
nums=[]
num=1
while len(nums)<M:
    nums.extend([num]*num)
    num+=1
print(sum(nums[N-1:M]))
    