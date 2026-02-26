import sys
input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))  # +, -, *, //

mx = -10**18
mn = 10**18

def div_truc(a,b):
    if a<0:
        return -(-a//b)
    return (a//b)
def dfs(idx,cur):
    global mx,mn
    if idx==N:
        mx=max(mx,cur)
        mn=min(mn,cur)
        return
    x=nums[idx]
    if ops[0]>0:
        ops[0]-=1
        dfs(idx+1,x+cur)
        ops[0] += 1
    if ops[1]>0:
        ops[1]-=1
        dfs(idx+1,cur-x)
        ops[1] += 1
    if ops[2]>0:
        ops[2]-=1
        dfs(idx+1,x*cur)
        ops[2] += 1
    if ops[3]>0:
        ops[3]-=1
        dfs(idx+1,div_truc(cur,x))
        ops[3] += 1
        
dfs(1,nums[0])
print(mx)
print(mn)
    