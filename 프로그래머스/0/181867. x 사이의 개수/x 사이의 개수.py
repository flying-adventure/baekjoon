def solution(myString):
    ans=[]
    k=0
    for i in myString:
        if i == "x":
            ans.append(k)
            k=0
        else:
            k+=1
    ans.append(k)
    return ans
            