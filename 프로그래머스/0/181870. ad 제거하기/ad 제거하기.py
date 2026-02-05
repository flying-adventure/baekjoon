def solution(strArr):
    ans=[]
    for i in strArr:
        if i in strArr:
            if not "ad" in i:
                ans.append(i)
    return ans