def solution(arr):
    ans=[]
    k=0
    for i in arr:
        while k<i:
            ans.append(i)
            k+=1
        k=0
    return ans
        
        