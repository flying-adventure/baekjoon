from collections import Counter
def solution(strArr):
    
    k=[]
    for i in strArr:
        k.append(len(i))
    cnt=Counter(k)
    return max(cnt.values())