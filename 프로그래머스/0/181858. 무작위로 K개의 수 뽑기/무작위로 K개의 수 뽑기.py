def solution(arr, k):
    seen=set()
    ans=[]
    for i in arr:
        if i not in seen:
            if len(ans)<k:
                ans.append(i)
                seen.add(i)
    while len(ans)<k:
        ans.append(-1)
    return ans