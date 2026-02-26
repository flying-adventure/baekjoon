def solution(numbers, target):
    a=len(numbers)
    ans=0
    def dfs(i,total):
        nonlocal ans
        if i==a:
            if total==target:
                ans+=1
            return
        dfs(i+1,total-numbers[i])
        dfs(i+1,total+numbers[i])
    dfs(0,0)
    return ans
    