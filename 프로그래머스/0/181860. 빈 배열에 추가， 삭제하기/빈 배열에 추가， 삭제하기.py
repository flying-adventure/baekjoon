def solution(arr, flag):
    ans=[]
    for i in range(len(arr)):
        if flag[i]==True:
            for k in range(arr[i]*2):
                ans.append(arr[i])
        if flag[i]==False:
            ans=ans[:-arr[i]]
    return ans
        